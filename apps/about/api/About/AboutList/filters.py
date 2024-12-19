import django_filters

from apps.about.models import About


class AboutFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Name bo'yicha qidiruv
    is_active = django_filters.BooleanFilter()  # is_active bo'yicha filter

    class Meta:
        model = About
        fields = ['name', 'is_active']
