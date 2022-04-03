from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.views import View
from userAuth.forms import LoginForm, SignupForm

User = get_user_model()

class LoginView(View):

    def get(self, request):
        self.login_form = LoginForm()
        return render(request, 'userAuth/login.html', {'login_form': self.login_form})

    def post(self, request):
        self.login_form = LoginForm(request.POST)
        if self.login_form.is_valid():
            return self.valid_form(request)
        else:
            return self.invalid_form(request)

    def valid_form(self, request):
        email = self.login_form.cleaned_data.get('username')
        password = self.login_form.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            self.login_form.add_error(None, "Invalid username or password")
            return render(request, 'userAuth/login.html', {'login_form': self.login_form})

    def invalid_form(self, request):
        return render(request, 'userAuth/login.html', {'login_form': self.login_form})

class SignupView(View):

    def get(self, request):
        self.signup_form = SignupForm()
        return render(request, 'userAuth/signup.html', {'signup_form': self.signup_form})

    def post(self, request):
        self.signup_form = SignupForm(request.POST)
        if self.signup_form.is_valid():
            return self.valid_form(request)
        else:
            return self.invalid_form(request)

    def invalid_form(self, request):
        return render(request, 'userAuth/signup.html', {'signup_form': self.signup_form})

    def valid_form(self, request):
        user = self.signup_form.save()
        email = self.signup_form.cleaned_data.get('email')
        password = self.signup_form.cleaned_data.get('password')
        login(request, user)
        return redirect("/")
