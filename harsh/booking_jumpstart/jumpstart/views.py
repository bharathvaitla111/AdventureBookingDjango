from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import LoginForm

# Create your views here.

class Login(View):
    def get(self, request):
        user_session = LoginForm()
        context = {'form': user_session}
        return render(request, 'jumpstart/login2.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is None:
                messages.error(request, "Incorrect username or password")
                return render(request, 'jumpstart/login.html', {'form': form})
        return render(request, 'jumpstart/login.html', {'form': form, 'user': user})

