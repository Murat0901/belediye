from django.urls import path
from .views import BlogPageView, AboutView, LatestPostDetail

urlpatterns = [
    path('', BlogPageView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('posts/<int:id>/', LatestPostDetail.as_view(), name="latestpost_detail")
]