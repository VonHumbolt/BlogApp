# Generated by Django 3.2 on 2021-08-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_postimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='postImage',
            field=models.ImageField(default='placeholder.jpg', upload_to='postImages'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]