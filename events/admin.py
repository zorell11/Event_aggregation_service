from django.contrib import admin

from .models import Category, Event, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comment)
