# apps/blog/urls.py

# Django modules
from django.urls import path

# My modules
from blog import views

# Namespace
app_name = 'blog'

urlpatterns = [
	path('', views.home_view, name='home'), 
]