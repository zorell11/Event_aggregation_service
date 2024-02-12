from rest_framework import serializers

from events.models import Event, Category, EventDate, Organizer

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class EventDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventDate
        fields = '__all__'


class OrganizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizer
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'address', 'company_name', 'company_ico']
