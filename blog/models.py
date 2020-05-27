from django.db import models

class BlogPost(models.Model):
    BlogTitle = models.CharField(max_length=100, verbose_name="Başlık")
    BlogImage = models.ImageField(upload_to='images/', null=True, blank=True)
    BlogContent = models.TextField(verbose_name="İçerik")
    BlogDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =  ['-BlogDate',]

    def __str__(self):
        return self.BlogTitle