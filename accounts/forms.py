from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Organizer

class UserSignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'address']



class OrganizerSignUpForm(UserCreationForm):
    class Meta:
        model = Organizer
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'address', 'company_name', 'bank_accunt', 'company_ico']


