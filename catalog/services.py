from django.core.cache import cache
from django.shortcuts import get_object_or_404

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получение данных продуктов из Кэша если кэш пустой получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return  products


def get_products_by_category_from_cache(category_slug):
    """
    Получение продуктов по категории из кэша.
    Если кэш пустой - получает данные из БД.
    """
    if not CACHE_ENABLED:
        return Product.objects.filter(category__slug=category_slug, is_active=True)

    key = f'products_category_{category_slug}'
    products = cache.get(key)

    if products is not None:
        return products

    # Получаем категорию и связанные с ней продукты
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_active=True)

    cache.set(key, products)
    return products


def get_categories_from_cache():
    """Получение всех категорий из кэша"""
    if not CACHE_ENABLED:
        return Category.objects.all()

    key = 'category_list'
    categories = cache.get(key)

    if categories is not None:
        return categories

    categories = Category.objects.all()
    cache.set(key, categories)
    return categories