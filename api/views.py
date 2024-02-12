from django.shortcuts import render
from rest_framework import mixins, generics
from events.models import Event, Category, EventDate, Organizer
from .serializers import EventSerializer, CategorySerializer, EventDateSerializer, OrganizerSerializer

from datetime import datetime
# Create your views here.


class Events(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer



    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Categories(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EventDates(mixins.ListModelMixin, generics.GenericAPIView):
    now = datetime.now().date()
    queryset = EventDate.objects.filter(date_to__gte=now)
    serializer_class = EventDateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Organizers(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
