from django.urls import path

from userAuth.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
]