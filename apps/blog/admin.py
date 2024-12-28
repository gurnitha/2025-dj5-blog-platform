# apps/blog/admin.py

# Django modules
from django.contrib import admin

# My modules
from blog import models

# Register your models here.

admin.site.register(models.Post)