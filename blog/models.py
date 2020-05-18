from django.db import models
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    BlogTitle = models.CharField(max_length=100, verbose_name="Başlık")
    BlogContent = RichTextField(verbose_name="İçerik")
    BlogDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.BlogTitle
