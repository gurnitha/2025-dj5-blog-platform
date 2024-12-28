# apps/blog/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home_view(request):
	data = {'section':'home'}
	return render(request, 'blog/home.html', data)


def about_view(request):
	data = {'section':'about'}
	return render(request, 'blog/about.html', data)