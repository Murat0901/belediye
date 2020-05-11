from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BlogPost


class BlogView(TemplateView):
    model = BlogPost
    template_name = "blog.html"
