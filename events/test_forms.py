from django.test import TestCase

from events.models import Organizer, Event, Category
from .forms import EventForm

from django import forms

import datetime

class EventsFromTest(TestCase):

    @classmethod
    def setUpTestData(self):
        Organizer.objects.create(
                username = 'organzier_user@user.sk',
                email = 'organzier_user@user.sk',
                password = 'pass',
                first_name = 'organzier_first_name',
                last_name = 'organzier_last_name',
                phone = '123456',
                address = 'organizer_test_address',
                company_name = 'organizer_test_company',
                bank_accunt = '12345678',
                company_ico = '123456'
            )
        Category.objects.create(name='Zabava')


    def test_event_form_is_valid(self):

        category = Category.objects.get(id=1)

        form = EventForm( data = {
            'event_name': 'Test event name',
            'place': 'Test event place',
            'address': 'Test event address',
            'description': 'Test event description',
            'category': category,
            'capacity': 200,
            'event_image': 'test_image.jpeg',
            'event_video': 'youtube.com/test_event',
            'ticket_price': 20,
            #'date_from': datetime.datetime(2024, 2, 11, 19, 30, tzinfo=datetime.timezone.utc),
            'date_from' : '2024-03-19 18:00:00+00:00',
            #'date_to': datetime.datetime(2024, 2, 11, 22, 0, tzinfo=datetime.timezone.utc),
            'date_to' : '2024-03-20 18:00:00+00:00',
        })

        self.assertTrue(form.is_valid())

    def test_event_form_date(self):
        category = Category.objects.get(id=1)
        form = EventForm( data = {
            'event_name': 'Test event name',
            'place': 'Test event place',
            'address': 'Test event address',
            'description': 'Test event description',
            'category': category,
            'capacity': 200,
            'event_image': 'test_image.jpeg',
            'event_video': 'youtube.com/test_event',
            'ticket_price': 20,
            'date_to' : '2024-03-19 18:00:00+00:00',
            'date_from' : '2024-03-20 18:00:00+00:00',
        })

        with self.assertRaises(forms.ValidationError):
            form.is_valid()
            form.clean()

    # today_date = str(datetime.datetime.today())
    # print(today_date)
    def test_event_form_date1(self, today_date=None):
        category = Category.objects.get(id=1)
        form = EventForm( data = {
            'event_name': 'Test event name',
            'place': 'Test event place',
            'address': 'Test event address',
            'description': 'Test event description',
            'category': category,
            'capacity': 200,
            'event_image': 'test_image.jpeg',
            'event_video': 'youtube.com/test_event',
            'ticket_price': 20,
            'date_to' : '2024-03-19 18:00:00+00:00',
            'date_from' : '2024-02-12 14:01:20.203478',
            #'date_from' : str(datetime.datetime.today()),
        })

        with self.assertRaises(forms.ValidationError):
            form.is_valid()
            form.clean()



    def test_event_form_date2(self):
        category = Category.objects.get(id=1)
        form = EventForm( data = {
            'event_name': 'Test event name',
            'place': 'Test event place',
            'address': 'Test event address',
            'description': 'Test event description',
            'category': category,
            'capacity': 200,
            'event_image': 'test_image.jpeg',
            'event_video': 'youtube.com/test_event',
            'ticket_price': 20,
            'date_to' : '2024-03-19 18:00:00+00:00',
            'date_from' : '2024-02-11 14:01:20.203478',
        })

        with self.assertRaises(forms.ValidationError):
            form.is_valid()
            form.clean()


