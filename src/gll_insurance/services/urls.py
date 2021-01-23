from django.urls import path
import services.views as views

app_name = 'services'

urlpatterns = [
	path('', views.index, name='services'),
]