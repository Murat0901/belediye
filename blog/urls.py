from django.urls import path
from .views import BlogView, BlogDetail

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:id>/', BlogDetail.as_view(), name="detail")
]