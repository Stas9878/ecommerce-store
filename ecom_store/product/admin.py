from django.contrib import admin
from .models import Category, Product, Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'created_by', 'rating', 'created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'total_items']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price', 'get_rating']
    list_display_links = ['name', 'price']
