from django.contrib.auth.models import User
from django.db import models
from django.forms import forms
from phonenumber_field.modelfields import PhoneNumberField


class Adventure(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    image = models.ImageField(upload_to='adventures')


class Booking(models.Model):
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    booking_date = models.DateTimeField(auto_now_add=True)


class User(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'), ]
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    phoneNumber = PhoneNumberField(unique=True, null=True, blank=False)
