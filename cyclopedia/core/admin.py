
from django.contrib import admin

from .models import Category, Subcategory, Entry


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ("category", "subcategory",)
    search_fields = ['title__name', 'category', 'subcategory']
