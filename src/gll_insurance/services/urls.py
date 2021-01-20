from django.urls import path
from .views import ServiceView

app_name = 'services'

urlpatterns = [
	path('', ServiceView.as_view(), name='services'),
]