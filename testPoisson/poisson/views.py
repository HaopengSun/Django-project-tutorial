from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    poissons = Poisson.objects.all()
    form = PoissonForm()

    if request.method == 'POST':
        form = PoissonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'poissons': poissons, 'form': form}

    return render(request, 'poisson/index.html', context)

def detail(request, pk):
    poisson = Poisson.objects.get(id=pk)
    area = Poisson.area(poisson)

    context = {'poisson': poisson, 'area': area}

    return render(request, 'poisson/detail.html', context)
