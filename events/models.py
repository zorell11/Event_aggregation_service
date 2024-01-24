from _ast import Pass

from django.db import models
from accounts.models import Organizer, CustomUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.id}. {self.name}'




class Event(models.Model):
    organizer_id = models.ForeignKey(Organizer, on_delete=models.DO_NOTHING, null=True, blank=False)
    event_name = models.CharField(max_length=128, blank=False, null=False)
    place = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=32, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=False)
    capacity = models.IntegerField(blank=False, null=False)
    event_image = models.ImageField(upload_to='images/', default=None, null=False, blank=False)
    event_video = models.CharField(max_length=128, null=True, blank=True)
    ticket_price = models.FloatField(null=False, blank=False)



    def __str__(self):
        #return f'{self.event_name} - {self.date_from}'
        #return f'{self.event_name} - {self.date_from.day}.{self.date_from.month}.{self.date_from.year}'
        return f'{self.event_name}'


class EventDate(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING, null=True, blank=False)
    date_from = models.DateTimeField(blank=False, null=False)
    date_to = models.DateTimeField(blank=True, null=True)


    def get_time_from(self):
            mins = '{:02}'.format(self.date_from.minute)
            hours = '{:02}'.format(self.date_from.hour)
            return f'{self.date_from.day}.{self.date_from.month}.{self.date_from.year} {hours}:{mins}'
    def get_time_to(self):
        mins = '{:02}'.format(self.date_to.minute)
        hours = '{:02}'.format(self.date_to.hour)
        return f'{self.date_to.day}.{self.date_to.month}.{self.date_to.year} {hours}:{mins}'


class Comment(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING, blank=False, null=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    #headline = models.CharField(max_length=64, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    # is_reply = models.BooleanField()
    # comment_id = models.IntegerField()
    comment_date = models.DateTimeField(auto_now_add=True)

class SigningUp(models.Model):
    PAYMENT_STATUS = [
        ("P", "Paid"),
        ("N", "Not paid"),
    ]
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING, blank=False, null=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    event_date = models.ForeignKey(EventDate, on_delete=models.SET_NULL, null=True)
    signing_up_date = models.DateTimeField(auto_now_add=True)
    ticket_count = models.IntegerField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=PAYMENT_STATUS, null=True)







