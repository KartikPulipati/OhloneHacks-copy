from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def home(requests):
    if requests.method == "GET":
        return render(requests, 'display/home.html')
    else:
        logout(requests)
        return redirect(reverse("login"))
