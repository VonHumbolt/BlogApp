# Generated by Django 3.2 on 2021-08-15 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='author',
            name='lastName',
        ),
    ]
