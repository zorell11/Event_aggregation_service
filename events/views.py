from django.shortcuts import render

from .models import Event

# Create your views here.



def index(request):
    events = Event.objects.all()
    content = {'events': events}
    return render(request, 'events/index.html', content)



def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    content = {'event': event}
    return render(request, 'events/event_detail.html', content)



