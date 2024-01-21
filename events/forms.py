from django import forms

from .models import Event, Category

from datetime import datetime, date, timedelta

class EventForm(forms.Form):
    #organizer_id = forms.ModelChoiceField(queryset=Organizer.objects)
    event_name = forms.CharField(max_length=128, required=True)
    place = forms.CharField(max_length=32, required=True)
    address = forms.CharField(max_length=32, required=True)
    date_from = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
    date_to = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
    description = forms.CharField(required=True)
    category = forms.ModelChoiceField(queryset=Category.objects)
    capacity = forms.IntegerField(min_value=1, required=True)
    event_image = forms.ImageField(required=False)
    event_video = forms.CharField(max_length=128, required=False)

    def clean(self):
        clean_data = super().clean()
        date_from = clean_data.get('date_from')
        print(10*'#')
        print(type(date_from))
        print(date_from)
        print(type(date_from.date()))
        print(date_from.date())
        print(date.today())
        print(type(date.today()))

        if clean_data.get('date_from') >= clean_data.get('date_to'):
            raise forms.ValidationError('Koniec podujatia nemože byť pred jej začiatkom!')
            return clean_data


        if date.today() == date_from.date():
            raise forms.ValidationError('Začiatok podujatia nemôže byť dnešný dátum!')
            return clean_data
        elif date.today() > date_from.date():
            raise forms.ValidationError('Začiatok podujatia nemôže byť z minulosti!')
            return clean_data





class AddEventCopyForm(forms.Form):
    date_from = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
    date_to = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
