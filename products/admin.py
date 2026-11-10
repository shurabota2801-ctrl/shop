from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAmdin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'updated', 'created']
    list_editable = ['price', 'available'] 
    list_filter = ['category', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAmdin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



