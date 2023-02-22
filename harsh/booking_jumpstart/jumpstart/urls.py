from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('forgot_password/', views.ForgotPassword.as_view(), name='forgot_password'),
]