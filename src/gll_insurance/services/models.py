from django.db import models

class Service(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	call_to_action = models.TextField()

	def __str__(self):
		return self.title

class ServiceList(models.Model):
	title = models.CharField(max_length=100)
	queryset = Service.objects.all()

	def __str__(self):
		return self.title