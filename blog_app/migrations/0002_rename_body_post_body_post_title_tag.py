# Generated by Django 4.0 on 2022-01-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='BODY',
            new_name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="J's Blog", max_length=255),
        ),
    ]
