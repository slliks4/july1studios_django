from django.urls import path
from .import views

urlpatterns = [
    path('', views.Gallery, name='gallery'),
    path('<str:category>',views.Gallery_others, name='gallery_others'),
    path('Recent/', views.Gallery_recent, name='gallery_recent'),
]