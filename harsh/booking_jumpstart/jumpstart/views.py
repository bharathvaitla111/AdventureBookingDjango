from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import LoginForm, RegistrationForm

# Create your views here.


class LoginSignup(View):
    def get(self, request):
        user_session = LoginForm()
        user_signup = RegistrationForm()
        context = {'form': user_session, 'signup': user_signup}
        return render(request, 'jumpstart/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        user_signup = RegistrationForm(request.POST)
        print(user_signup.is_valid())
        print(form)
        if form.is_valid() and 'first_name' not in request.POST.keys():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is None:
                print('hehe')
                messages.error(request, "Incorrect username or password")
                return render(request, 'jumpstart/login.html', {'form': form})
            return render(request, 'jumpstart/welcome.html', {'form': form, 'user': user})

        elif user_signup.is_valid():
            print('login inside valid')
            user_signup.save()
            form.email = user_signup.cleaned_data['email']
            return render(request, 'jumpstart/login.html', {'form': form})


class Welcome(View):
    def get(self, request):
        return render(request, 'jumpstart/welcome.html')

    def post(self, request):
        return render(request, 'jumpstart/welcome.html')

