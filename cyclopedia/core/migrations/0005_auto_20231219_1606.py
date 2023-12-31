# Generated by Django 3.2.23 on 2023-12-19 13:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20231219_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entry',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='owner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='price',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
