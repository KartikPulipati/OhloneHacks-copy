from glob import escape
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from userAuth.forms import GardenForm
class LoginView(View):

    def get(self, request):
        self.garden_form = GardenForm()
        return render(request, 'userAuth/login.html', {'garden_form': self.garden_form})

    def post(self, request):
        self.garden_form = GardenForm(request.POST)
        breakpoint()
        if self.garden_form.is_valid():
            return self.valid_form(request)
        else:
            return self.invalid_form(request)

    def valid_form(self, request):
        email = self.garden_form.cleaned_data.get('username')
        password = self.garden_form.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            self.garden_form
            return render(request, 'userAuth/login.html', {'garden_form': self.garden_form})

    def invalid_form(self, request):
        return render(request, 'userAuth/login.html', {'garden_form': self.garden_form})