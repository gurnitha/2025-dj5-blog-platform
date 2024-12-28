# apps/blog/views.py

# Django modules
from django.shortcuts import render

# My modules
from blog.models import Post 

# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    data = {
        'section':'home',
        'posts':posts,
    }
    return render(request, 'blog/home.html', data)


def about_view(request):
    data = {'section':'about'}
    return render(request, 'blog/about.html', data)