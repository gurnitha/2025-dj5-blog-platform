# apps/blog/models.py

# Django modules
from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(default='', max_length=255)
	body = models.TextField(default='', blank=True)

	def __str__(self):
		return self.title