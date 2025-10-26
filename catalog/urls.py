from django.urls import path
from . import views

app_name= 'catalog'


urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('electronics/', views.electronics, name='electronics'),
    path('cloth/', views.cloth, name='cloth'),
    path('house-garden/', views.house_garden, name='house_garden'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]