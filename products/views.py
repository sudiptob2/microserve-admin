from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from products.models import Product
from products.producer import Producer
from products.serializers import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    """Handle creating and listing of products."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        producer = Producer()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        producer.publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductByIDAPIView(RetrieveUpdateDestroyAPIView):
    """API View for product retrieve, delete and update by ID."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        producer = Producer()
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        producer.publish('product_updated', serializer.data)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        producer = Producer()
        instance = self.get_object()
        self.perform_destroy(instance)
        producer.publish('product_deleted', kwargs['id'])
        return Response(status=status.HTTP_204_NO_CONTENT)
