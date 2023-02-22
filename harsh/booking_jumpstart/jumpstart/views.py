from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from . import views
from django.contrib.auth import authenticate
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .forms import LoginForm
from .models import Customer

# Create your views here.

class Login(View):
    def get(self, request):
        user_session = LoginForm()
        context = {'form': user_session}
        return render(request, 'jumpstart/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            if authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password']) is None:
                messages.error(request, "Incorrect username or password")
            else:
                messages.success(request, 'success')

        return render(request, 'jumpstart/login.html', {'form': form})

