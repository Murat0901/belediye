from django.urls import path
from .views import HomePageView, AboutView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
]