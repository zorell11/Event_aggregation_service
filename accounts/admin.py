from django.contrib import admin
from .models import CustomUser, Organizer


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Organizer)


