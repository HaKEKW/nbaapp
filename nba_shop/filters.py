import django_filters
from django_filters import DateFilter, CharFilter

from nba_shop.models import Good


class GoodFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Good
        fields = ['category', 'name', 'description']