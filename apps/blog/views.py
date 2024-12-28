# apps/blog/views.py

# Django modules
from django.shortcuts import render, get_object_or_404, redirect

# My modules
from blog.models import Post 
from blog.forms import CreatePostForm

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


def post_create_view(request):

    # Handling POST request
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:home')

    # Handling GET request
    else:
        form = CreatePostForm()

    data = {
        'title':'Add new post',
        'section':'blog_create',
        'form':form,
    }

    return render(request, 'blog/create.html', data)


def post_edit_view(request, pk=None):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', slug=post.slug)

    else:
        form = CreatePostForm(instance=post)

    data = {
        'title':'Edit post',
        'section':'blog_edit',
        'post':post,
        'form':form,
    }

    return render(request, 'blog/edit.html', data)


def about_view(request):
    data = {'section':'about'}
    return render(request, 'blog/about.html', data)