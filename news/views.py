from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogPageView(ListView):
    model = Post
    template_name = "index.html"