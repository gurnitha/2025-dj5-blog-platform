# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # blog
    path('', include('blog.urls', namespace='blog')),
    # django-allauth
    path('accounts/', include('allauth.urls')),
    # admin
    path('admin/', admin.site.urls),
]
