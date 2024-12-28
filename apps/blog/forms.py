# apps/blog/forms.py

# Django modules
from django.forms import ModelForm

# My modules
from blog.models import Post 

# Create your forms here.

class CreatePostForm(ModelForm):

	class Meta:
		model = Post
		fields = ['title','body','slug']