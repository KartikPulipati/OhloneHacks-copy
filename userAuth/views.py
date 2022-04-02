from glob import escape
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from userAuth.forms import GardenForm
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(View):

    def get(self, request):
        self.garden_form = GardenForm()
        return render(request, 'login.html', {'garden_form': self.garden_form})

    def post(self, request):
        self.garden_form = GardenForm(request.POST)
        if self.garden_form.is_valid():
            return self.valid_form(request)
        else:
            return self.invalid_form(request)

    def valid_form(self, request):
        return redirect("home")
    
    def invalid_form(self, request):
        return render(request, 'login.html', {'garden_form': self.garden_form})

class GardenAuthBackend(ModelBackend):
    def authenticate(self, **credentials):
        return 'username' in credentials and self.authenticate_by_username_or_email(**credentials)
    
    def authenticate_by_username_or_email(self, username=None, password=None):
        breakpoint()
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
        if user:
            b = user if user.check_password(password) else None
            print(b)
            return b
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None