from django.shortcuts import render

from django.views.generic import CreateView
from django.urls import reverse_lazy

from events.models import Event
from .forms import UserSignUpForm, OrganizerSignUpForm

from .models import Organizer


# Create your views here.


def user_profile(request):
    pass



class UserSignUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('index')
    template_name = 'user_signup.html'


class OrganizerSignUpForm(CreateView):
    form_class = OrganizerSignUpForm
    success_url = reverse_lazy('index')
    template_name = 'organizer_signup.html'


def user_profile(request):
    #user = Organizer.objects.get(id=request.user.id)
    events = Event.objects.filter(organizer_id=request.user)
    content ={'events': events}
    return render(request, 'user_profile.html', content)

