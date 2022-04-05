from typing import List

from django.urls import path

from products.views import ProductByIDAPIView, ProductListCreateAPIView

app_name = 'products'

urlpatterns: List[str] = [
    path(
        'products/',
        ProductListCreateAPIView.as_view(),
        name='product_list_create_api_view',
    ),
    path(
        'products/<int:id>',
        ProductByIDAPIView.as_view(),
        name='product_api_view_by_id',
    ),
]
