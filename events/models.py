from _ast import Pass

from django.db import models
from accounts.models import Organizer


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.id}. {self.name}'

class Comment(models.Model):
    pass

class Event(models.Model):
    organizer_id = models.ForeignKey(Organizer, on_delete=models.DO_NOTHING, null=False, blank=False)
    event_name = models.CharField(max_length=128, blank=False, null=False)
    place = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=32, blank=False, null=False)
    date_from = models.DateTimeField(blank=False, null=False)
    date_to = models.DateTimeField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=False, blank=False)
    capacity = models.IntegerField(blank=False, null=False)
    event_image = models.ImageField(upload_to='images/', default=None, null=False, blank=False)
    event_video = models.CharField(max_length=128, null=True, blank=True)


