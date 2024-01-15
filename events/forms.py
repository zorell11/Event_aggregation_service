from django import forms

from accounts.models import Organizer
from .models import Event, Category



class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    def clean(self):
        return super().clean()


# class EventForm(forms.Form):
#     organizer_id = forms.ModelChoiceField(queryset=Organizer.objects)
#     event_name = forms.CharField(max_length=128, required=True)
#     place = forms.CharField(max_length=32, required=True)
#     address = forms.CharField(max_length=32, required=True)
#     date_from = forms.DateField(widget=forms.SelectDateWidget, required=True)
#     date_to = forms.DateField(widget=forms.SelectDateWidget, required=True)
#     description = forms.CharField(required=True)
#     category = forms.ModelChoiceField(queryset=Category.objects)
#     capacity = forms.IntegerField(required=True)
#     event_image = forms.ImageField(required=False)
#     event_video = forms.CharField(max_length=128, required=False)
#
#     def clean(self):
#         return super().clean()
