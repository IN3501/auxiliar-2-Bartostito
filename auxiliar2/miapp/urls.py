
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('pestaña/', views.pestaña, name='pestaña'),
	path('docentes/', views.docentes, name='docentes'),
	
]


