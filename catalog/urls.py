from django.urls import path
from .views import (
    HomeView, ContactsViev, ElectronicsView,
    ClothView, HouseGardenView, ProductDetailView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsViev.as_view(), name='contacts'),
    path('electronics/', ElectronicsView.as_view(), name='electronics'),
    path('cloth/', ClothView.as_view(), name='cloth'),
    path('house-garden/', HouseGardenView.as_view(), name='house_garden'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]