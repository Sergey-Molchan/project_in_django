from django.contrib.auth.decorators import permission_required
from django.views.decorators.cache import cache_page

from . import views
from django.urls import path
from .views import (
    HomeView, ContactsView, ElectronicsView,
    ClothView, HouseGardenView, ProductDeleteView, ProductCreateView,
    ProductDetailView, ProductUpdateView, ProductPublishView, CategoryProductListView, ProductListView
)

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Исправил название
    path('electronics/', ElectronicsView.as_view(), name='electronics'),
    path('cloth/', ClothView.as_view(), name='cloth'),
    path('house-garden/', HouseGardenView.as_view(), name='house_garden'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/publish/', permission_required('catalog.can_unpublish_product')(ProductPublishView.as_view()), name='product_publish'),
    path('category/<slug:category_slug>/', CategoryProductListView.as_view(), name='category_products'),
    path('products/', ProductListView.as_view(), name='product_list'),
  
]
