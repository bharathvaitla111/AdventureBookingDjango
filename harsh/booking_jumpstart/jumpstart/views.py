from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from . import views

from .forms import LoginForm

# Create your views here.


class Login(View):
    def get(self, request):
        user_session = LoginForm()
        context = {'form': user_session}
        return render(request, 'jumpstart/check_login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        print(request.POST)
        messages.error(request, 'Account created successfully')
        return render(request, 'jumpstart/check_login.html', {'form': form})

class ForgotPassword(View):
    def get(self, request):
        return render(request, 'jumpstart/forgot_password.html', {})

    def post(self, request):
        return render(request, 'jumpstart/forgot_password.html')