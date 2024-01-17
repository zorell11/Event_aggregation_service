from django.shortcuts import render

from .models import Event, Category

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


