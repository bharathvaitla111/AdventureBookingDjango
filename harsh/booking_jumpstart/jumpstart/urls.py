from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginSignup.as_view(), name='login'),
    path('', views.Welcome.as_view(), name='welcome'),
    path('forgot_password/', views.ForgotPassword.as_view(), name='forgot'),
]
