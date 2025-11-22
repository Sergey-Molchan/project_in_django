from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product
from django.views.generic import UpdateView, DetailView, CreateView, TemplateView, ListView, DeleteView
from .forms import ProductForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .mixins import OwnerRequiredMixin, OwnerOrModeratorMixin
from django.db import models


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_count'] = Category.objects.count()
        context['products_count'] = Product.objects.count()
        return context


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ElectronicsView(ListView):
    template_name = 'electronics.html'
    context_object_name = 'electronics_products'

    def get_queryset(self):
        # Показываем только опубликованные продукты
        return Product.objects.filter(category__name='Электроника', status='published')


class ClothView(ListView):
    template_name = 'cloth.html'
    context_object_name = 'clothing_products'

    def get_queryset(self):
        # Показываем только опубликованные продукты
        return Product.objects.filter(category__name='Одежда', status='published')


class HouseGardenView(ListView):
    template_name = 'house_garden.html'
    context_object_name = 'house_garden_products'

    def get_queryset(self):
        # Показываем только опубликованные продукты
        return Product.objects.filter(category__name='Дом и сад', status='published')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_queryset(self):
        # Базовый queryset - только опубликованные продукты
        queryset = Product.objects.filter(status='published')

        # Если пользователь аутентифицирован и имеет права, показываем все
        if self.request.user.is_authenticated:
            user = self.request.user
            if user.has_perm('catalog.can_unpublish_product'):
                return Product.objects.all()

        return queryset

    def get_object(self, queryset=None):
        """Переопределяем получение объекта для проверки прав владельца"""
        obj = super().get_object(queryset)

        # Если продукт не опубликован, проверяем права доступа
        if obj.status != 'published' and self.request.user.is_authenticated:
            user = self.request.user
            if user != obj.owner and not user.has_perm('catalog.can_unpublish_product'):
                from django.http import Http404
                raise Http404("Продукт не найден")

        return obj


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_kwargs(self):
        """Передаем пользователя в форму"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Автоматически устанавливаем владельца
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

    def get_form_kwargs(self):
        """Передаем пользователя в форму"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, OwnerOrModeratorMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


# Новые представления для работы со статусами продуктов
class ProductListView(ListView):
    """Список всех продуктов (для модераторов и владельцев)"""
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Для модераторов и владельцев показываем все продукты
        # Для остальных - только опубликованные
        if self.request.user.is_authenticated:
            user = self.request.user
            if user.has_perm('catalog.can_unpublish_product'):
                return Product.objects.all()
            # Владельцы видят свои продукты + опубликованные
            return Product.objects.filter(
                models.Q(owner=user) | models.Q(status='published')
            )
        return Product.objects.filter(status='published')


class ProductPublishView(LoginRequiredMixin, OwnerOrModeratorMixin, UpdateView):
    """Публикация/отмена публикации продукта"""
    model = Product
    fields = []  # Только меняем статус
    template_name = 'product_confirm_publish.html'

    def form_valid(self, form):
        product = self.get_object()
        if product.status == 'published':
            # Отмена публикации - проверяем права
            if not self.request.user.has_perm('catalog.can_unpublish_product'):
                raise PermissionDenied("У вас нет прав для отмены публикации")
            product.status = 'draft'
        else:
            # Публикация - может владелец
            if product.owner != self.request.user:
                raise PermissionDenied("Только владелец может публиковать продукт")
            product.status = 'published'

        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})
