
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Contact_us, name='contact'),
]
