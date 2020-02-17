from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost

class BlogPageView(ListView):
    model = BlogPost
    template_name = "blog.html"