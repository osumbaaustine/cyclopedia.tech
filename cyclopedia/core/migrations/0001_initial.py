# Generated by Django 3.2.23 on 2023-12-19 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AIBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('categories', models.ManyToManyField(to='core.AI')),
            ],
        ),
        migrations.CreateModel(
            name='AISolutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('categories', models.ManyToManyField(to='core.AI')),
            ],
        ),
        migrations.CreateModel(
            name='AIPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('owner', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='core.AIBlog')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='AICommunities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('categories', models.ManyToManyField(to='core.AI')),
            ],
        ),
    ]
