# Generated by Django 5.0.6 on 2024-05-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feisbucc', '0005_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_post',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='media/blank-profile-picture.png', upload_to=''),
        ),
    ]
