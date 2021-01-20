from django.shortcuts import render
from django.views.generic import ListView
from .models import Service

class ServiceView(ListView):
	model = Service
	template_name = 'services/index.html'

	def get_queryset(self):
		return Service.objects.all()