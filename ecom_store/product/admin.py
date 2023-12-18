from django.contrib import admin
from .models import Category, Product, Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'rating', 'created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

