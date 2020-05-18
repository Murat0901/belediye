from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView

class BlogView(ListView):
    template_name = 'blog.html'
    queryset = BlogPost.objects.all()


