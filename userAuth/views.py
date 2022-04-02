from glob import escape
from django.shortcuts import render
from django.views import View
from userAuth.forms import GardenForm
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

        return render(request, 'login.html', {'garden_form': self.garden_form})