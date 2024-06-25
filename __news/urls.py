from django.urls import path
from .import views

urlpatterns = [
    path('', views.News_page, name='news'),
    path('readmore/<str:slug>', views.News_readmore, name='readmore'),
]
