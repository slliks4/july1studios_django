from django.urls import path
from .import views

urlpatterns = [
    path('', views.Application, name='application'),
    path('Career/', views.Career_opportunity, name='career')
]