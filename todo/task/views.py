from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
	# return HttpResponse('hello world')

	tasks = Task.objects.all()
	context = {'tasks': tasks}

	return render(request, 'task/list.html', context)