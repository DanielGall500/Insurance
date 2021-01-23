from django.shortcuts import render
from django.views.generic import ListView
from .models import Service, ServiceList

class ServiceView(ListView):
	model = Service
	template_name = 'services/index.html'

	def get_queryset(self):
		return Service.objects.all()

def index(request):
	services_list = Service.objects.all()
	context = { 'services_list' : services_list }
	return render(request, 'services/index.html', context)