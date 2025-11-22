from . import views
from django.urls import path
from .views import (
    HomeView, ContactsView, ElectronicsView,
    ClothView, HouseGardenView, ProductDeleteView, ProductCreateView,
    ProductDetailView, ProductUpdateView
)

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Исправил название
    path('electronics/', ElectronicsView.as_view(), name='electronics'),
    path('cloth/', ClothView.as_view(), name='cloth'),
    path('house-garden/', HouseGardenView.as_view(), name='house_garden'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/publish/', views.ProductPublishView.as_view(), name='product_publish'),
]