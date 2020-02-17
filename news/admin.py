from django.contrib import admin
from .models import Post, LatestPost

admin.site.register(Post)
admin.site.register(LatestPost)