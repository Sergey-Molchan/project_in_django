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