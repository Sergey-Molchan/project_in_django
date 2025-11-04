from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import UpdateView, DetailView, CreateView, TemplateView, ListView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_count'] = Category.objects.count()
        context['products_count'] = Product.objects.count()
        return context


class ContactsViev(TemplateView):
    template_name = 'contacts.html'


class ElectronicsView(ListView):
    template_name = 'electronics.html'
    context_object_name = 'electronics_products'

    def get_queryset(self):
        return Product.objects.filter(category__name='Электроника')


class ClothView(ListView):
    template_name = 'cloth.html'
    context_object_name = 'clothing_products'

    def get_queryset(self):
        return Product.objects.filter(category__name='Одежда')


class HouseGardenView(ListView):
    template_name = 'house_garden.html'
    context_object_name = 'house_garden_products'

    def get_queryset(self):
        return Product.objects.filter(category__name='Дом и сад')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
