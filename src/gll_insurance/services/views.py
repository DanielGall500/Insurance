from django.shortcuts import render
from django.views.generic.detail import ListView
from .models import Service

class ServiceView(ListView):
	model = Service
