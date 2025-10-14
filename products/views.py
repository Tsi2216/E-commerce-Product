from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from core.permissions import IsOwnerOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    # Added default ordering to avoid pagination warning
    queryset = Product.objects.filter(is_active=True).select_related('category', 'owner').order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    filterset_fields = ['category__id', 'owner__id']
    ordering_fields = ['price', 'created_at']
    ordering = ['id']  # Default ordering for list view
