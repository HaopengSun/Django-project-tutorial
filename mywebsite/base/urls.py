from django.urls import path
from . import views

# use home function in the views
urlpatterns = [
	path('', views.home)
]