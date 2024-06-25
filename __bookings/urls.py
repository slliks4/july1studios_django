
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Booking, name='booking'),
    path('Submit/', views.Base, name='base'),
]
