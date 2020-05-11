from django.db import models


class BlogPost(models.Model):
    BlogTitle = models.CharField(max_length=100, verbose_name="Başlık")
    BlogContent = models.TextField(verbose_name="İçerik")
    BlogDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.BlogTitle
