from django import forms

from .models import Event, Category, EventDate

from datetime import date


def event_date_checks(clean_data, date_from):
    if clean_data.get('date_from') >= clean_data.get('date_to'):
        raise forms.ValidationError('Koniec podujatia nemože byť pred jej začiatkom!')
        return clean_data
    elif date.today() == date_from.date():
        raise forms.ValidationError('Začiatok podujatia nemôže byť dnešný dátum!')
        return clean_data
    elif date.today() > date_from.date():
        raise forms.ValidationError('Začiatok podujatia nemôže byť z minulosti!')
        return clean_data

    return None


class EventForm(forms.Form):
    #organizer_id = forms.ModelChoiceField(queryset=Organizer.objects)
    event_name = forms.CharField(max_length=128, required=True, label="Meno eventu")
    place = forms.CharField(max_length=128, required=True, label="Miesto")
    address = forms.CharField(max_length=64, required=True, label="Adresa")
    date_from = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'),
            label="Od:")
    date_to = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'),
            label="Do:")
    category = forms.ModelChoiceField(queryset=Category.objects, label='Kategória')
    capacity = forms.IntegerField(min_value=1, required=True, label='Kapacita divákov')
    ticket_price = forms.FloatField(min_value=1, required=True, label='Cena lístka')
    event_image = forms.ImageField(required=False, label='Obrázok')
    event_video = forms.CharField(max_length=128, required=False, label='Video(nepovinné)')
    description = forms.CharField(min_length=20, required=True, widget=forms.Textarea, label='Popis podujatia')


    def clean(self):
        clean_data = super().clean()
        date_from = clean_data.get('date_from')

        checks = event_date_checks(clean_data, date_from)
        if checks != None:
            return checks



class AddEventCopyForm(forms.Form):
    date_from = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
    date_to = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))

    def clean(self):
        clean_data = super().clean()
        date_from = clean_data.get('date_from')

        checks = event_date_checks(clean_data, date_from)
        if checks != None:
            return checks

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'place', 'address', 'category', 'capacity', 'ticket_price', 'event_video', 'description']


class UpdateEventDate(forms.ModelForm):

    date_from = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
    date_to = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))

    class Meta:
        model = EventDate
        fields = '__all__'
        #fields = ['id', 'date_from', 'date_to']

    def clean(self):
        clean_data = super().clean()
        date_from = clean_data.get('date_from')

        checks = event_date_checks(clean_data, date_from)
        if checks != None:
            return checks

