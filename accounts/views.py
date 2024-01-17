from django.shortcuts import render

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserSignUpForm, OrganizerSignUpForm

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

