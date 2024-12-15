from django_filters import rest_framework as filters

from apps.contact.models import Contact


class ContactFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive name search
    phone_number = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive phone number search
    email = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive email search
    created_at = filters.DateFromToRangeFilter()  # Filter by a range of creation dates
    is_active = filters.BooleanFilter(field_name='is_active', label='Is Active')

    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'created_at', 'is_active']
