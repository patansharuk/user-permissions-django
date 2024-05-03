from django.urls import path
from .views import index, create_products, delete_product

urlpatterns = [
    path('', index, name='index_path'),
    path('create',create_products, name='create_product_path'),
    path('<int:product_id>/destroy',delete_product, name='delete_product_path'),
]
