from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(User):
    class Meta:
        ordering = ['first_name']
        verbose_name_plural = 'customer'

    city = models.CharField(max_length=30)
    contact_number = PhoneNumberField(null=False, blank=True, unique=True)

    def __str__(self):
        return self.username
