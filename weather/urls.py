from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.weather, name='home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city')
]
