from django.urls import path
from .views import EmailView

urlpatterns = [
    path('', EmailView, name='contact'),
]