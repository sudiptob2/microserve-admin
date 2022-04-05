from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from products.models import Product
from products.serializers import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    """Handle creating and listing of products."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductByIDAPIView(RetrieveUpdateDestroyAPIView):
    """API View for product retrieve, delete and update by ID."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
