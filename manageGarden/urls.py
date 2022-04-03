from django.contrib import admin
from django.urls import path, include
from manageGarden import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('create/', views.createPlant, name='createPlant')
]