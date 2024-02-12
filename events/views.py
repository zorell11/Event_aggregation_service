from builtins import print
from concurrent.futures._base import LOGGER

from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Event, Category, Comment, Organizer, EventDate, SigningUp

from .forms import EventForm, AddEventCopyForm, EditEventForm, UpdateEventDate

from django.urls import reverse


from datetime import datetime, date, timezone, timedelta

# Create your views here.


def check_not_paid_tickets():
    tickets = SigningUp.objects.filter(status='N')
    actual_time = datetime.now().replace(tzinfo=timezone.utc)
    for ticket in tickets:
        pay_time = ticket.signing_up_date + timedelta(minutes=15)
        if pay_time < actual_time:
            ticket.delete()


def index(request):
    data = {}
    event_dates = EventDate.objects.filter(date_to__gt=datetime.now()).order_by('date_from')
    for date in event_dates:
        if date.event_id.id not in data:
            data[date.event_id.id] = date
    content = {'data': data}

    # events = Event.objects.all()
    # event_dates = EventDate.objects.all()
    # content = {'events': events, "event_dates":  event_dates, 'data': data}
    return render(request, 'events/index.html', content)



def event_detail(request, pk):
    check_not_paid_tickets()
    event = Event.objects.get(id=pk)
    event_dates = EventDate.objects.filter(event_id=pk, date_to__gte=datetime.now().date()).order_by('date_from')
    event_date_free_tickets = {}
    for event_date in event_dates:
        tickets_sold = SigningUp.objects.filter(event_id=pk, event_date=event_date.id).aggregate(Sum('ticket_count'))['ticket_count__sum']
        tickets_sold = 0 if tickets_sold == None else tickets_sold
        event_date_free_tickets[event_date.id] = event.capacity-tickets_sold
    comments = Comment.objects.filter(event_id=pk).order_by('-comment_date')
    content = {'event': event, 'event_dates': event_dates, 'comments': comments, 'event_date_free_tickets': event_date_free_tickets}
    return render(request, 'events/event_detail.html', content)


def event_category(request, name):
    try:
        category = Category.objects.get(name=name)
    except Category.DoesNotExist:
        category = None
        print('No category in database')

    events = Event.objects.filter(category=category)

    content = {'events': events, 'category': category}
    return render(request, 'events/index.html', content)

@login_required
def add_comment(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        print(request.POST)
        event_id = request.POST.get('event_id')
        event_obj = Event.objects.get(id=event_id)
        comment = request.POST.get('comment').strip()
        if comment:
            Comment.objects.create(event_id=event_obj, user_id=user, comment=comment)

    return redirect(f'/event/{event_id}')

def search(request):
    searched_word = request.POST.get('search')
    if searched_word == None:
        searched_word = ""
    #searched_words = searched_word.split(' ')
    found_events = []
    events = Event.objects.filter(event_name__contains=searched_word)
    for event in events:
        event_date = event.event_date.filter(date_to__gt=datetime.now()).order_by('date_from')
        if event_date:
            found_events.append(event)
    content = {'events': found_events, 'searched_word': searched_word}
    return render(request, 'events/search.html', content)


def advanced_search(request):
    searched_word = request.POST.get('search')
    if searched_word == None:
        searched_word = ""

    searched_date = request.POST.get('date')
    print(searched_date)

    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    found_events = []
    events = Event.objects.filter(event_name__contains=searched_word)
    if searched_date == 'today':
        for event in events:
            found_event = event.event_date.filter(date_from__day=day, date_from__month=month, date_from__year=year)
            print(found_event)
            if found_event:
                found_events.append(event)

    elif searched_date == 'this_week':
        current_week = date.today().isocalendar().week
        for event in events:
            #found_event = EventDate.objects.filter(date_from__week=current_week)
            found_event = event.event_date.filter(date_from__week=current_week, date_to__gt=datetime.now()).order_by('date_from')

            if found_event:
                found_events.append(event)
        print(found_events)


    elif searched_date == 'this_month':
        for event in events:
            found_event = event.event_date.filter(date_from__month=month, date_from__year=year)
            print(found_event)
            if found_event:
                found_events.append(event)

    elif searched_date == 'next_month':
        for event in events:
            found_event = event.event_date.filter(date_from__month=month+1, date_from__year=year)
            print(found_event)
            if found_event:
                found_events.append(event)

    else:
        for event in events:
            event_date = event.event_date.filter(date_to__gt=datetime.now()).order_by('date_from')
            if event_date:
                found_events.append(event)

    print(found_events)
    content = {'events': found_events, 'searched_word': searched_word}
    return render(request, 'events/search.html', content)


def available_ticket(request):
    event_id = int(request.POST.get('event_id'))
    event_date_id = int(request.POST.get('event_date'))
    event = Event.objects.get(id=event_id)
    tickets_sold = SigningUp.objects.filter(event_id=event_id, event_date=event_date_id).aggregate(Sum('ticket_count'))['ticket_count__sum']
    if tickets_sold == None:
        tickets_sold = 0
    return event.capacity - tickets_sold


@login_required
def add_num_ticket(request):
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        event_id = int(request.POST.get('event_id'))
        event_date_id = int(request.POST.get('event_date'))
        event = Event.objects.get(id=event_id)
        event_date = EventDate.objects.get(id=event_date_id)
        available_tickets = available_ticket(request)
        content = {'event': event, 'event_date':event_date,'available_tickets': available_tickets}
        return render(request, 'events/choose_tickets.html', content)

@login_required
def shopping_cart(request):
    check_not_paid_tickets()
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        event_id = int(request.POST.get('event_id'))
        event_date_id = int(request.POST.get('event_date'))
        ticket_num = int(request.POST.get('ticket_num'))
        try:
            ticket_booked = SigningUp.objects.get(user_id=user, event_id=event_id, event_date_id=event_date_id, status='N')
            print(ticket_booked.ticket_count)
            new_ticket_count = ticket_num + ticket_booked.ticket_count
            ticket_booked.ticket_count = new_ticket_count
            ticket_booked.save()
        except :
            event = Event.objects.get(id=event_id)
            event_date = EventDate.objects.get(id=event_date_id)
            SigningUp.objects.create(
                event_id = event,
                user_id = user,
                event_date = event_date,
                ticket_count = ticket_num,
                status = 'N'
            )

    orders = SigningUp.objects.filter(user_id=user,status='N')
    full_price = 0
    tickets_price = 0
    for order in orders:
        tickets_price += order.event_id.ticket_price*order.ticket_count
    print(orders)
    content = {'orders': orders, 'tickets_price':tickets_price, 'full_price': tickets_price+0.5}
    return render(request, 'events/shopping_cart.html', content)


#### forms:


class PersonCreateView(FormView):
    template_name = 'events/create_event.html'
    form_class = EventForm
    #success_url = reverse_lazy('event_detail', kwargs={'pk': self.pk})



    def form_valid(self, form):
        self.pk = 1
        user = Organizer.objects.get(email=self.request.user)
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data

        new_event = Event.objects.create(
            organizer_id = user,
            event_name = cleaned_data['event_name'],
            place = cleaned_data['place'],
            address = cleaned_data['address'],
            description = cleaned_data['description'],
            capacity = cleaned_data['capacity'],
            event_image = cleaned_data['event_image'],
            event_video = cleaned_data['event_video'],
            category = cleaned_data['category'],
            ticket_price = cleaned_data['ticket_price'],
        )
        self.pk = new_event.id

        new_date = EventDate.objects.create(
            event_id = new_event,
            date_from = cleaned_data['date_from'],
            date_to = cleaned_data['date_to']
        )
        #return result
        return super(PersonCreateView, self).form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

class AddEventCopyView(FormView):
    template_name = 'events/add_event_copy.html'
    form_class = AddEventCopyForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        event = Event.objects.get(id=pk)
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        print(cleaned_data['date_from'])
        EventDate.objects.create(
            event_id = event,
            date_from = cleaned_data['date_from'],
            date_to = cleaned_data['date_to']
        )
        return result


@login_required
def order_success(request):
    user = request.user
    orders = SigningUp.objects.filter(user_id=user,status='N')
    for order in orders:
        order.status = 'P'
        order.save()
    if request.method == 'POST':
        return render(request, 'events/order_success.html')


@login_required
def remove_single_ticket(request, pk):
    signingup = SigningUp.objects.get(id=pk)
    new_ticket_count = signingup.ticket_count -1
    if new_ticket_count:
        signingup.ticket_count = new_ticket_count
        signingup.save()
    else:
        signingup.delete()
    return redirect('shopping_cart')

@login_required
def remove_all_tickets(request, pk):
    signingup = SigningUp.objects.get(id=pk)
    signingup.delete()
    return redirect('shopping_cart')


@login_required
def update_event(request, pk):
    event = Event.objects.get(id=pk)
    print(request.POST)
    if request.method == 'POST':
        form = EditEventForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            event.event_name = cleaned_data['event_name']
            event.place = cleaned_data['place']
            event.address = cleaned_data['address']
            event.category = cleaned_data['category']
            event.capacity = cleaned_data['capacity']
            event.ticket_price = cleaned_data['ticket_price']
            event.event_video = cleaned_data['event_video']
            event.event_video = cleaned_data['event_video']

            event.save()
            return redirect('event_detail', pk=pk)


    event = Event.objects.get(id=pk)
    form = EditEventForm(instance=event)
    content = {'form': form, 'event': event}
    return render(request, 'events/update_event.html', content)


@login_required
def update_event_date(request, pk):
    pk = int(pk)
    event_date = EventDate.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateEventDate(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            event_date.date_from = cleaned_data['date_from']
            event_date.date_to = cleaned_data['date_to']
            event_date.save()
            return redirect('event_detail', pk=event_date.event_id.id)
        else:
            print('invalid')
    else:
        event_date = EventDate.objects.get(id=pk)
        form = UpdateEventDate(instance=event_date)
    content = {'form': form, 'event_date': event_date}
    return render(request, 'events/update_event_date.html', content)
