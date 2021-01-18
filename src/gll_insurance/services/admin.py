from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_filter = ('title',)
	search_fields = ('title',)

admin.site.register(Service, ServiceAdmin)