from django.shortcuts import render, redirect
from manageGarden.models import plant
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def dashboard(request):
    plants = plant.objects.filter(users=request.user)
    return render(request, 'manageGarden/dashboard.html', {'plants': plants})

# @login_required(login_url='login')
def createPlant(request):
    if request.method == 'GET':
        return render(request, 'manageGarden/create.html')
    else:
        newtodo = plant.objects.create(users=request.user, name=request.POST['name'],
                                       water_consumption=request.POST['water'], output=request.POST['output'])
        newtodo.user = request.user
        newtodo.save()
        return redirect('dashboard')

