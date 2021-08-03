from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

from .forms import *

# Create your views here.
def index(request):
	# return HttpResponse('hello world')

	tasks = Task.objects.all()
	form = TaskForm()

	# when users submit a new todo, save it and redirect
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks': tasks, 'form': form}

	return render(request, 'task/list.html', context)

def update(request, pk):
	task = Task.objects.get(id=pk)

	#prefill the form
	form = TaskForm(instance=task)

	if request.method == 'POST':
		# instance means we need to update a specific todo instead of creating a new one
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}

	return render(request, 'task/update.html', context)