from concurrent.futures._base import LOGGER

from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy

from .models import Event, Category

from .forms import EventForm

# Create your views here.



def index(request):
    events = Event.objects.all()
    content = {'events': events }
    return render(request, 'events/index.html', content)



def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    content = {'event': event}
    return render(request, 'events/event_detail.html', content)


def event_category(request, name):
    category = Category.objects.get(name=name)
    print(category.name)
    events = Event.objects.filter(category=category)
    content = {'events': events, 'category': category}
    return render(request, 'events/index.html', content)




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


class PersonCreateView(CreateView):
    template_name = 'events/create_event.html'
    form_class = EventForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data')
        return super().form_invalid(form)




# class PersonCreateView(FormView):
#     template_name = 'events/create_event.html'
#     form_class = EventForm
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cleaned_data = form.cleaned_data
#         new_event = Event.objects.create(
#             organizer_id = cleaned_data['organizer_id'],
#             event_name = cleaned_data['event_name'],
#             place = cleaned_data['place'],
#             address = cleaned_data['address'],
#             date_from = cleaned_data['date_from'],
#             date_to = cleaned_data['date_to'],
#             description = cleaned_data['description'],
#             capacity = cleaned_data['capacity'],
#             event_image = cleaned_data['event_image'],
#             event_video = cleaned_data['event_video'],
#             category = cleaned_data['category'],
#         )
#
#         #new_event.organizer_id.set(cleaned_data['organizer_id'])
#         #new_event.category.set(cleaned_data['category'])
#
#         return result

    # def form_invalid(self, form):
    #     LOGGER.warning('User provided invalid data')
    #     return super().form_invalid(form)



