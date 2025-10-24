from django.shortcuts import render
from .models import Category, Product

def home(request):
    categories_count = Category.objects.count()
    products_count = Product.objects.count()
    context = {
        'categories_count': categories_count,
        'products_count': products_count,
    }
    return render(request, 'home.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def electronics(request):
    electronics_products = Product.objects.filter(category__name='Электроника')
    context = {
        'electronics_products': electronics_products
    }
    return render(request, 'electronics.html', context)

def cloth(request):
    clothing_products = Product.objects.filter(category__name='Одежда')
    context = {
        'clothing_products': clothing_products
    }
    return render(request, 'cloth.html', context)

def house_garden(request):
    house_garden_products = Product.objects.filter(category__name='Дом и сад')
    context = {
        'house_garden_products': house_garden_products
    }
    return render(request, 'house_garden.html', context)