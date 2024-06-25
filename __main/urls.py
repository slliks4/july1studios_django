
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('services/', views.Services, name='services'),
    path('how_we_work/', views.How_we_work, name='how_we_work'),
    path('why_us/', views.Why_us, name='why_us'),
]
