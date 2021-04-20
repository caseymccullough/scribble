"""scribble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("posts/", views.post_list, name="post_list"),
    path('posts/<int:pk>', views.post_detail, name="post_detail" ), # take that int and assign to pk
    path('comments/', views.comment_list, name="comment_list"),
    path('comments/<int:pk>', views.comment_detail, name="comment_detail"),
    path('comments/new', views.comment_create, name="comment_create"),
    path('comments/<int:pk>/edit', views.comment_edit, name="comment_edit"),
    path('comments/<int:pk>/delete', views.comment_delete, name="comment_delete"),
    path('posts/new', views.post_create, name="post_create"),
    path('posts/<int:pk>/edit', views.post_edit, name="post_edit"),
    path('posts/<int:pk>/delete', views.post_delete, name="post_delete"),
    

]
