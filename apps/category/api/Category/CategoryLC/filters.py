from django_filters import rest_framework as filters

from apps.category.models import Category


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    is_active = filters.BooleanFilter(field_name='is_active')
    slug = filters.CharFilter(field_name='slug', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name', 'is_active', 'slug']
