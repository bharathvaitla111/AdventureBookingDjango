from django.forms import ModelForm
from .models import Customer
from django.forms import EmailInput, PasswordInput
from django import forms


class LoginForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'password']
        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter a valid email address',
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter your password'
            })
        }
