from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
]