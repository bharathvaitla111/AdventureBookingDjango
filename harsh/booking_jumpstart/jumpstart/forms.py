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
                'class': "u-border-2 u-border-grey-75 u-input u-input-rectangle u-palette-3-light-3 u-radius-22 u-input-1",
                'placeholder': 'Enter a valid email address',
            }),
            'password': PasswordInput(attrs={
                'class': "u-border-2 u-border-grey-75 u-input u-input-rectangle u-palette-3-light-3 u-radius-22 u-input-2",
                'placeholder': 'Enter your password'
            })
        }
