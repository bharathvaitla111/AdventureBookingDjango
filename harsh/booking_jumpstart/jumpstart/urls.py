from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('', views.Welcome.as_view(), name='welcome'),
]
