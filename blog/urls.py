from django.urls import path
from .views import BlogView

urlpatterns = [
    path('blog/', BlogView, name='blog'),
]