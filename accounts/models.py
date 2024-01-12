from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.EmailField(null=False, blank=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.TextField(null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Organizer(CustomUser):
    organzier = models.BooleanField(default=True)
    company_name = models.TextField(null=False, blank=False)
    bank_accunt = models.CharField(max_length=32, null=False, blank=False)
    company_ico = models.CharField(max_length=32, null=True, blank=True)


    class Meta:
        verbose_name_plural = "Organizers"
