# Generated by Django 4.0 on 2022-01-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_profile_facebook_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
