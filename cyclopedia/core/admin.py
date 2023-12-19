# from django.contrib import admin
# from .models import Category, SubCategory, Entry
#
#
# admin.site.register(Category, SubCategory)
#
#

# admin.py
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
