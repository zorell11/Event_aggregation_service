from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Organizer

from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Heslo',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Heslo znova',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_('Enter the same password as before, for verification.'),
    )
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'address']
        labels = {
            'first_name': 'Meno',
            'last_name': 'Priezvisko',
            'password1': 'Heslo',
            'phone': 'Telefónne číslo',
            'address': 'Adresa',
            'password1': 'Heslo',
            'password2': 'Heslo znova',
        }

class OrganizerSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Heslo',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Heslo znova',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_('Enter the same password as before, for verification.'),
    )
    class Meta:
        model = Organizer
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'address', 'company_name', 'bank_accunt', 'company_ico']
        labels = {
            'first_name': 'Meno',
            'last_name': 'Priezvisko',
            'password1': 'Heslo',
            'phone': 'Telefónne číslo',
            'address': 'Adresa',
            'company_name': 'Meno firmy',
            'bank_accunt': 'Číslo bankového účtu',
            'company_ico': 'IČO',
        }

