from django.db import models
from poisson.algorithm import canvas

class Poisson(models.Model):
	title = models.CharField(max_length=200)
	discription = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	width = models.IntegerField(default=800)
	height = models.IntegerField(default=800)

	def __str__(self):
		return self.title

	def canvasArea(self):
		return canvas(self.width, self.height)