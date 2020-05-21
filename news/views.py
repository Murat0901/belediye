from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import LatestPost


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogPageView(ListView):
    model = LatestPost
    template_name = "index.html"

class LatestPostDetail(DetailView):
    model = LatestPost
    template_name = "posts/latestpost_detail.html"
    queryset = LatestPost.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(LatestPost, id=id_)