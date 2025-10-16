from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # ← id и name как в ТЗ!

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # ← id, name, price, category
    list_filter = ('category',)  # ← фильтрация по категории
    search_fields = ('name', 'description')  # ← поиск по name и description