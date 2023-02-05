# Register your models here.
from django.contrib import admin
from django.db import models
from .models import Adventure, Booking, User

# Register your models here.
admin.site.register(Adventure)
admin.site.register(Booking)
admin.site.register(User)
