from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Service, ServiceList

class ServiceView(generic.ListView):
	model = Service
	template_name = 'services/index.html'

	context_object_name = 'services_list'
	def get_queryset(self):
		return Service.objects.all()

def description(request, pk):
	service = get_object_or_404(Service, pk=pk)
	services_list = Service.objects.all()
	context = { 'service' : service,
				'services_list' : services_list }
	return render(request, 'services/description.html', context=context)
