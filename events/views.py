from concurrent.futures._base import LOGGER

from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Event, Category, Comment, Organizer, EventDate, SigningUp

from .forms import EventForm, AddEventCopyForm

from django.urls import reverse

# Create your views here.



def index(request):
    events = Event.objects.all()
    content = {'events': events }
    return render(request, 'events/index.html', content)



def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    event_dates = EventDate.objects.filter(event_id=pk)
    # event = Event.objects.get(id=pk).event_name
    # event = Event.objects.filter(event_name=event)
    comments = Comment.objects.filter(event_id=pk).order_by('-comment_date')
    content = {'event': event, 'event_dates': event_dates, 'comments': comments}
    return render(request, 'events/event_detail.html', content)
    #return render(request, 'events/test.html', content)


def event_category(request, name):
    category = Category.objects.get(name=name)
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



from django.db.models import Sum
def add_num_ticket(request):
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        event_id = int(request.POST.get('event_id'))
        event_date_id = int(request.POST.get('event_date'))
        event = Event.objects.get(id=event_id)
        event_date = EventDate.objects.get(id=event_date_id)
        tickets_sold = SigningUp.objects.filter(event_id=event_id, event_date=event_date_id, status='P').aggregate(Sum('ticket_count'))['ticket_count__sum']
        print(tickets_sold)
        print(100*'#')
        if tickets_sold == None:
            tickets_sold = 0
        available_tickets = event.capacity - tickets_sold
        content = {'event': event, 'event_date':event_date ,'available_tickets': available_tickets}
        return render(request, 'events/choose_tickets.html', content)


from django.core.exceptions import ObjectDoesNotExist
def shopping_cart(request):
    user = request.user
    print(type(user))
    if request.method == 'POST':

        print(request.POST)
        event_id = int(request.POST.get('event_id'))
        event_date_id = int(request.POST.get('event_date'))
        ticket_num = int(request.POST.get('ticket_num'))
        try:
            ticket_booked = SigningUp.objects.get(user_id=user, event_id=event_id, event_date_id=event_date_id, status='N')
            print(ticket_booked.ticket_count)
            new_ticket_count = ticket_num + ticket_booked.ticket_count
            #ticket_booked.update(ticket_count=new_ticket_count)
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
    print(orders)
    content = {'orders': orders}


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

        print(self.pk)
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
        # user = event.organizer_id
        EventDate.objects.create(
            event_id = event,
            date_from = cleaned_data['date_from'],
            date_to = cleaned_data['date_to']
        )

        return result
