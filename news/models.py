from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LatestPost(models.Model):
    LatestTitle = models.CharField(max_length=100, verbose_name="Başlık")
    LatestImage = models.ImageField(upload_to='images/', null=True)
    LatestContent = RichTextField(verbose_name="İçerik")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.LatestTitle