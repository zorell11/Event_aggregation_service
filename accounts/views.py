from django.shortcuts import render

from django.views.generic import CreateView
from django.urls import reverse_lazy

from events.models import Event, SigningUp
from .forms import UserSignUpForm, OrganizerSignUpForm
from django.contrib.auth.decorators import login_required


from .models import Organizer


# Create your views here.

class UserSignUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('index')
    template_name = 'user_signup.html'


class OrganizerSignUpForm(CreateView):
    form_class = OrganizerSignUpForm
    success_url = reverse_lazy('index')
    template_name = 'organizer_signup.html'

@login_required
def user_profile(request):
    #user = Organizer.objects.get(id=request.user.id)
    events = Event.objects.filter(organizer_id=request.user)
    tickets = SigningUp.objects.filter(user_id=request.user, status='P')

    content ={'events': events, 'tickets':tickets}
    return render(request, 'user_profile.html', content)

