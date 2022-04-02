from django.urls import path
from display import views

urlpatterns = [
    path('', views.home, name="home")
]