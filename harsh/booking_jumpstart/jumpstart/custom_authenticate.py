from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class EmailAuth(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            customer = User.objects.get(email=email)
            if password != customer.password and password is not None:
                return None
        except ObjectDoesNotExist as e:
            return None
        return customer
