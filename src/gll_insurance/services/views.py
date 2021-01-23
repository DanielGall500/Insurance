from django.shortcuts import render, get_object_or_404
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

def description(request, pk):
	service = get_object_or_404(Service, pk=pk)
	context = { 'service' : service }
	return render(request, 'services/description.html', context=context)
