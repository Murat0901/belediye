# Generated by Django 3.0.5 on 2020-05-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_delete_contactpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PageTitle', models.CharField(max_length=30, verbose_name='Başlık')),
                ('tel', models.CharField(max_length=20, verbose_name='Telefon')),
            ],
        ),
    ]