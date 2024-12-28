# apps/blog/views.py

# Django modules
from django.shortcuts import render, get_object_or_404

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


def post_detail_view(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    data = {
        'section':'Post detail',
        'post':post,
    }
    return render(request, 'blog/detail.html', data)

def about_view(request):
    data = {'section':'about'}
    return render(request, 'blog/about.html', data)