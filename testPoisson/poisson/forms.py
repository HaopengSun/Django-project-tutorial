from django import forms
from django.forms import ModelForm

from .models import *

class PoissonForm(forms.ModelForm):

	class Meta:
		model = Poisson
		fields = '__all__'