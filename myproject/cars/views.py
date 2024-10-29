from rest_framework import viewsets, permissions
from .models import *
from .seiralizers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarsFilter
from rest_framework.filters import SearchFilter,OrderingFilter


class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
    filterset_class = CarsFilter
    search_fields = ['cars_name']
    ordering_fields = ['cars_name', 'price', 'year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]