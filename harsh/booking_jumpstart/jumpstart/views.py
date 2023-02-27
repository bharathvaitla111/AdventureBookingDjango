from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import LoginForm, RegistrationForm, Forgot

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
        if form.is_valid() and 'first_name' not in request.POST.keys():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is None:
                messages.error(request, "Incorrect username or password")
                return render(request, 'jumpstart/login.html', {'form': form})
            return render(request, 'jumpstart/welcome.html', {'form': form, 'user': user})

        elif user_signup.is_valid():
            user_signup.save()
            form.email = user_signup.cleaned_data['email']
            return render(request, 'jumpstart/login.html', {'form': form})


class Welcome(View):
    def get(self, request):
        return render(request, 'jumpstart/welcome.html')


class ForgotPassword(View):

    def get(self, request):
        user_forgot = Forgot()
        reset = None
        context = {'form': user_forgot, 'reset': reset}
        return render(request, 'jumpstart/forgot_password.html', context)

    def post(self, request):
        form = Forgot(request.POST)
        reset = None
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return HttpResponseRedirect(reverse('login'))
        elif reset is None:
            user = authenticate(email=form.cleaned_data['email'])
            if user is None:
                messages.error(request, "Incorrect email")
                return render(request, 'jumpstart/forgot_password.html', {'form': form, 'reset': reset})
            else:
                reset = Forgot()
                reset.initial['email'] = form.cleaned_data['email']
                messages.success(request, "proceed to reset")
                return render(request, 'jumpstart/forgot_password.html', {'reset': reset})

