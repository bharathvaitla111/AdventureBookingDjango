from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class EmailAuth(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            customer = User.objects.get(email=email)
            if password is not None and not customer.check_password(password):
                return None
        except ObjectDoesNotExist as e:
            return None
        return customer
