# Generated by Django 3.0.1 on 2020-01-29 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_latestpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latestpost',
            old_name='latestTitle',
            new_name='LatestTitle',
        ),
    ]
