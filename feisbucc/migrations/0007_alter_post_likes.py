# Generated by Django 5.0.6 on 2024-05-28 23:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feisbucc', '0006_alter_post_image_post_alter_profile_profile_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]