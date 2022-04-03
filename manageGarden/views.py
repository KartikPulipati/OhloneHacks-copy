from django.shortcuts import render, redirect
from manageGarden.models import plant
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    plants = plant.objects.filter(users=request.user)
    total_water = 0
    o = {}
    for p in plants:
        total_water += p.water_consumption
        o[p.name] = p.output

    return render(request, 'manageGarden/dashboard.html', {'plants': plants, 'w': total_water, 'o': o})

@login_required(login_url='login')
def createPlant(request):
    if request.method == 'GET':
        return render(request, 'manageGarden/create.html')
    else:
        newplant = plant.objects.create(users=request.user, name=request.POST['name'],
                                       water_consumption=request.POST['water'], output=request.POST['output'])
        newplant.user = request.user
        newplant.save()
        return redirect('dashboard')

