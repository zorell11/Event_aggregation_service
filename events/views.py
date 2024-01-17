from concurrent.futures._base import LOGGER

from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Event, Category, Comment, Organizer

from .forms import EventForm, AddEventCopyForm

# Create your views here.



def index(request):
    events = Event.objects.all()
    content = {'events': events }
    return render(request, 'events/index.html', content)



def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    #event = Event.objects.get(id=pk).event_name
    #event = Event.objects.filter(event_name=event)
    comments = Comment.objects.filter(event_id=pk).order_by('-comment_date')
    content = {'event': event, 'comments': comments}
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




#### forms:


# def event_image_view(request):
#
#     if request.method == 'POST':
#         form = EventForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = EventForm()
#     return render(request, 'events/create_event.html', {'form': form})


# class PersonCreateView(CreateView):
#     template_name = 'events/create_event.html'
#     form_class = EventForm
#     success_url = reverse_lazy('index')
#
#     def form_invalid(self, form):
#         LOGGER.warning('User provided invalid data')
#         return super().form_invalid(form)




class PersonCreateView(FormView):
    template_name = 'events/create_event.html'
    form_class = EventForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        user = Organizer.objects.get(email=self.request.user)
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        # if cleaned_data['date_from'] >= cleaned_data['date_to']:
        #     LOGGER.warning('User provided invalid data')
        #     return super().form_invalid(form)
        print(cleaned_data['date_from'])
        new_event = Event.objects.create(
            organizer_id = user,
            event_name = cleaned_data['event_name'],
            place = cleaned_data['place'],
            address = cleaned_data['address'],
            date_from = cleaned_data['date_from'],
            date_to = cleaned_data['date_to'],
            description = cleaned_data['description'],
            capacity = cleaned_data['capacity'],
            event_image = cleaned_data['event_image'],
            event_video = cleaned_data['event_video'],
            category = cleaned_data['category'],
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data')
        return super().form_invalid(form)


class AddEventCopyView(FormView):
    template_name = 'events/add_event_copy.html'
    form_class = AddEventCopyForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        pk = self.kwargs.get('jojo')
        print(pk)
        event = Event.objects.get(id=pk)
        print(event)
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        print(cleaned_data['date_from'])
        print(cleaned_data['date_to'])
        print(event.organizer_id)
        print(event.id)
        print(event.event_name)
        print(event.place)
        print(event.address)
        print(event.description)
        print(event.capacity)
        print(event.category)
        user = Organizer.objects.get(email=event.organizer_id)
        print(user)
        new_event = Event.objects.create(
            organizer_id = user,
            event_name = event.event_name,
            place = event.place,
            address = event.address,
            date_from = cleaned_data['date_from'],
            date_to = cleaned_data['date_to'],
            description = event.description,
            capacity = event.capacity,
            event_image = event.event_image,
            event_video = event.event_video,
            category = event.category,
        )

        return result
