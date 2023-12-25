# from django.db import models
from django.contrib.auth.models import User
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=50)
#
#     @staticmethod
#     def get_all_categories():
#         return Category.objects.all()
#
#     def __str__(self):
#         return self.name
#
#
# class SubCategory(models.Model):
#     name = models.TextField(max_length=50)
#     categories = models.ManyToManyField(Category)
#
#
# class Entry(models.Model):
#     thumbnail = models.ImageField(upload_to='images', blank=True, null=True)
#     title = models.CharField(max_length=200, unique=True)
#     # category = models.CharField(max_length=200)
#     category = models.ManyToManyField(SubCategory)
#     slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
#     owner = models.CharField(max_length=200)
#     price = models.CharField(max_length=200)
#     description = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#
#     class Meta:
#         ordering = ['-created_on']
#
#     def __str__(self):
#         return self.title
#
#
# # class Comment(models.Model):
# #     post = models.ForeignKey(AIBlog, on_delete=models.CASCADE, related_name='comments')
# #     name = models.CharField(max_length=80)
# #     email = models.EmailField()
# #     body = models.TextField()
# #     created_on = models.DateTimeField(auto_now_add=True)
# #     active = models.BooleanField(default=False)
# #
# #     class Meta:
# #         ordering = ['created_on']
# #
# #     def __str__(self):
# #         return 'Comment {} by {}'.format(self.body, self.name)
#
#


# models.py
from django.db import models
from django.utils.text import slugify
import django_filters


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')


    def __str__(self):
        return f"{self.category} - {self.name}"


class Entry(models.Model):
    thumbnail = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=200, default='No Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    author = models.CharField(max_length=200, default='')
    owner = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(default='', blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate the slug based on the title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# class EntryFilter(django_filters.FilterSet):
#     class Meta:
#         model = Entry
#         fields = ['Category', 'Subcategory', 'Author']
