# Generated by Django 3.0.5 on 2020-05-20 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200521_0216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-BlogDate']},
        ),
    ]