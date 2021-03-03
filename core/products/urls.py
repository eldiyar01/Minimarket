from django.urls import path, include
from .views import *

app_name = 'products'
urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>', product_detail, name='product'),
    path('category-products/<int:pk>', category_products, name='category_products'),
    path('product/buy/>', buy, name='buy'),
    path('products/', search, name='search')
]
