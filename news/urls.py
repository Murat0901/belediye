from django.urls import path
from .views import BlogPageView, AboutView, BlogView

urlpatterns = [
    path('', BlogPageView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
]