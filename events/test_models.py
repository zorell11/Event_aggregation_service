from django.test import TestCase

from .models import Event, Category, Organizer, EventDate, SigningUp
import datetime
from django.db import IntegrityError


class EventsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Organizer.objects.create(
            username='organzier_user@user.sk',
            email='organzier_user@user.sk',
            password='pass',
            first_name='organzier_first_name',
            last_name='organzier_last_name',
            phone='123456',
            address='organizer_test_address',
            company_name='organizer_test_company',
            bank_accunt='12345678',
            company_ico='123456'
        )

        user = Organizer.objects.get(id=1)
        category = Category.objects.create(name='Zabava')
        Event.objects.create(
            organizer_id=user,
            event_name='Test event name',
            place='Test event place',
            address='Test event address',
            description='Test event description',
            category=category,
            capacity=200,
            event_image='test_image.jpeg',
            event_video='youtube.com/test_event',
            ticket_price=20
        )

        event_id = Event.objects.get(id=1)
        EventDate.objects.create(
            event_id=event_id,
            date_from=datetime.datetime(2024, 2, 11, 19, 30, tzinfo=datetime.timezone.utc),
            date_to=datetime.datetime(2024, 2, 11, 22, 0, tzinfo=datetime.timezone.utc)
        )

    def test_event_name(self):
        event = Event.objects.get(id=1)
        self.assertEqual(event.event_name, 'Test event name')

    def test_organizer_email(self):
        organizer = Organizer.objects.get(id=1)
        self.assertEqual(organizer.email, 'organzier_user@user.sk')

    def test_event_date_get_time_from(self):
        event_date = EventDate.objects.get(id=1)
        self.assertEqual(event_date.get_time_from(), '11.2.2024 19:30')

    def test_event_date_get_time_to(self):
        event_date = EventDate.objects.get(id=1)
        self.assertEqual(event_date.get_time_to(), '11.2.2024 22:00')

    def test_sold_tickets(self):
        event = Event.objects.get(event_name='Test event name')
        num_sold_tickets = SigningUp.objects.filter(event_id=event).count()
        self.assertEqual(num_sold_tickets, 0)

    def test_category_unique(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(name='Zabava')
