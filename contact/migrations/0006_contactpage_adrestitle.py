# Generated by Django 3.0.5 on 2020-05-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contactpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='adresTitle',
            field=models.CharField(max_length=50, null=True, verbose_name='Adres Adı'),
        ),
    ]
