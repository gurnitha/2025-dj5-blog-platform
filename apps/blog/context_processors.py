# apps/blog/context_processors.py

# My modules
from blog.models import Post

def latest_posts(request):
	posts = Post.objects.filter().order_by('-date')[:3]
	return {'latest_posts': posts}