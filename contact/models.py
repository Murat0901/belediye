from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ad Soyad", null=True)
    title = models.CharField(max_length=50, verbose_name="Başlık")
    email = models.EmailField(verbose_name="E-Posta Adresiniz")
    message = models.TextField(verbose_name="Mesajınız")

    def __str__(self):
        return self.title

