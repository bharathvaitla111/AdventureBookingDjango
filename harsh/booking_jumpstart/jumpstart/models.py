from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(User):
    class Meta:
        ordering = ['first_name']
        verbose_name_plural = 'customer'

    def __str__(self):
        return self.username


class Booking(models.Model):
    TICKET_CHOICES = [
        ('Adult', '1000'),
        ('Child', '600'),
        ('FastTrackAdult', '2000'),
        ('FastTrackChild', '1200'),
        ('SeniorCitizen', '800'),
        ('AdultCollegeIdOffer', '900'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bookingDate = models.DateField()
    reserveDate = models.DateField()
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    typeOfTicketAndPrice = models.CharField(max_length=20, choices=TICKET_CHOICES)
    totalPrice = models.PositiveIntegerField(default=0)
    adultTicketCount = models.PositiveIntegerField(default=0)
    ChildTicketCount = models.PositiveIntegerField(default=0)
    FastTrackAdultTicketCount = models.PositiveIntegerField(default=0)
    FastTrackChildTicketCount = models.PositiveIntegerField(default=0)
    SeniorCitizenTicketCount = models.PositiveIntegerField(default=0)
    AdultCollegeIdOfferTicketCount = models.PositiveIntegerField(default=0)







