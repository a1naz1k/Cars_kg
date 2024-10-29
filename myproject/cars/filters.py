from django_filters import FilterSet
from .models import Cars


class CarsFilter(FilterSet):
    class Meta:
        model = Cars
        fields = {
            'type_change': ['exact'],
            'year': ['exact'],
            'volume': ['exact'],
            'color': ['exact'],
            'price': ['gt', 'lt'],
            'marka': ['exact'],
        }