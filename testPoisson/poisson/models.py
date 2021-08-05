from django.db import models
from poisson.algorithm import canvas

class Poisson(models.Model):
	title = models.CharField(max_length=200)
	discription = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	unitsize = models.FloatField(default=0.05)
	width = models.IntegerField(default=800)
	height = models.IntegerField(default=800)
	sievesize = models.CharField(max_length=120, default='4.75, 2.36, 1.18, 0.6, 0.3')
	minimumradius = models.IntegerField(default=1)
	finerpercent = models.CharField(max_length=120, default='1, 0.92, 0.82, 0.58, 0.14')
	voidratio = models.FloatField(default=0.8)
	cellsize = models.IntegerField(default=1)
	density = models.FloatField(default=0.001631)

	def __str__(self):
		return self.title

	def canvasArea(self):
		return canvas(self.width, self.height)