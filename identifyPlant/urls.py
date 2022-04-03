from django.contrib import admin
from django.urls import path, include
from identifyPlant import views

urlpatterns = [
    path('', views.identify, name='identify'),
]