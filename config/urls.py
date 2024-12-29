# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # blog
    path('', include('blog.urls', namespace='blog')),
    # django-allauth
    path('accounts/', include('allauth.urls')),
    # admin
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)