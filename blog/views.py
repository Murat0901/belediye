from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.views.generic import ListView, DetailView

class BlogView(ListView):
    template_name = 'blog.html'
    queryset = BlogPost.objects.all()

class BlogDetail(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"
    queryset = BlogPost.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)