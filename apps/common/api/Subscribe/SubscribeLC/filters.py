from django_filters import rest_framework as filters

from apps.common.models import Subscribe


class SubscribeFilterSet(filters.FilterSet):
    email = filters.CharFilter(field_name='email', lookup_expr='icontains', label='Email')
    url = filters.CharFilter(field_name='url', lookup_expr='icontains', label='URL')
    is_active = filters.BooleanFilter(field_name='is_active', label='Is Active')

    class Meta:
        model = Subscribe
        fields = ['email', 'url', 'is_active']
