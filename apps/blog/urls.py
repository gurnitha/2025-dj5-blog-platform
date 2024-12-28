# apps/blog/urls.py

# Django modules
from django.urls import path

# My modules
from blog import views

# Namespace
app_name = 'blog'

urlpatterns = [
	path('', views.home_view, name='home'),
	path('post/create/', views.post_create_view, name='create'),
	path('post/edit/<int:pk>/', views.post_edit_view, name='edit'),
	path('post/delete/<int:pk>/', views.post_delete_view, name='delete'), 
	path('post/<slug:slug>/', views.post_detail_view, name='detail'), 
	path('about/', views.about_view, name='about'), 
]