from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(EventDate)

@admin.register(SigningUp)
class SigningUpAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'user_id', 'event_date', 'signing_up_date', 'ticket_count', 'status']
    search_fields = ['signing_up_date', 'ticket_count']
