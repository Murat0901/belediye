from django.urls import path
from .views import BlogPageView

urlpatterns = [
    path('blog/', BlogPageView.as_view(), name='blog'),
]