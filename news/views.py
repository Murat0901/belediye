from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post, LatestPost, BlogPost

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogPageView(ListView):
    model = LatestPost
    template_name = "index.html"

class BlogView(TemplateView):
    model = BlogPost
    template_name = "blog.html"