# apps/blog/models.py

# Django modules
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User 

# Third party modules
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    title = models.CharField(default='', max_length=255)
    slug = models.SlugField(
            default='', 
            max_length=255, 
            blank=True,
            help_text='Live it blank. It will be automatically fill in once post title is added.')
    body = models.TextField(default='', blank=True)
    author = models.ForeignKey(
            User, 
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    '''
    By overriding the save method we can execute custom logic before the
    object is stored in the database. The slugify function converts a string to
    a URL slug (“My blog title” string becomes “my-blog-title”). We have to call
    super().save(*args, **kwargs) to execute the default saving behavior
    and store the object in the database.
    '''
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    '''
    The get_absolute_url method tells Django how to calculate the canonical
    URLforanobject. The reverse method returns a path reference that matches
    the view name and parameters.
    '''
    def get_absolute_url(self):
        return reverse(
            'blog:detail', args=[str(self.slug)]
        )