from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.EmailField(null=False, blank=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=256, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def print_username(self):
        username, domain = self.email.split('@')
        return username

    def get_billing_information(self):
        return f'{self.first_name} {self.last_name}\n{self.address}\n{self.phone}'

class Organizer(CustomUser):
    organzier = models.BooleanField(default=True)
    company_name = models.CharField(max_length=64, null=False, blank=False)
    bank_accunt = models.CharField(max_length=32, null=False, blank=False)
    company_ico = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = "Organizers"
