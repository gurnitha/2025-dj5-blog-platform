# apps/blog/views.py

# Django modules
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator

# Third party module
from taggit.models import Tag

# My modules
from blog.models import Post 
from blog.forms import CreatePostForm

# Create your views here.

def home_view(request, tag=None):
    tag_obj = None

    if not tag:
        posts = Post.objects.all()

    else:
        tag_obj = get_object_or_404(Tag, slug=tag)
        posts = Post.objects.filter(tags__in=[tag_obj])

    # Pagination
    '''
    The Paginator class allows us to split a QuerySet into parts. Pass in the
     objects you want paginate and the number of items you would like to have
     on each page.
    '''
    paginator = Paginator(posts, 1)
    '''
    We use request.GET.get('page') to get the current page
    number. The page parameter is assigned using a Query string (?page=1). 
    '''
    page = request.GET.get('page')
    '''
    The posts = paginator.get_page(page) line makes the page items 
    available through the posts object.
    '''
    posts = paginator.get_page(page)

    data = {
        'section':'home',
        'posts':posts,
        'tag': tag_obj,
    }

    return render(request, 'blog/home.html', data)


def post_detail_view(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    data = {
        'section':'Post detail',
        'post':post,
    }
    return render(request, 'blog/detail.html', data)


@permission_required('blog.create', raise_exception=True)
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


@permission_required('blog.edit', raise_exception=True)
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


@permission_required('blog.delete', raise_exception=True)
def post_delete_view(request, pk=None):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('blog:home')

    else:
        form = CreatePostForm(instance=post)

    data = {
        'title':'Delete post',
        'section':'blog_delete',
        'post':post,
        'form':form,
    }

    return render(request, 'blog/delete.html', data)


def about_view(request):
    data = {'section':'about'}
    return render(request, 'blog/about.html', data)