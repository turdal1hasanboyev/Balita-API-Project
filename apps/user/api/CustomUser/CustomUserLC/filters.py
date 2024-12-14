from django_filters import rest_framework as filters

from apps.user.models import CustomUser

from datetime import date


class CustomUserFilterSet(filters.FilterSet):
    age_min = filters.NumberFilter(method='filter_age_min', label='Minimum Age')
    age_max = filters.NumberFilter(method='filter_age_max', label='Maximum Age')
    gender = filters.ChoiceFilter(choices=CustomUser.GENDER, label='Gender')
    is_active = filters.BooleanFilter(field_name='is_active', label='Is Active')
    
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'gender',
            'is_active',
        ]

    def filter_age_min(self, queryset, name, value):
        return queryset.filter(birthday__lte=date(date.today().year - value, date.today().month, date.today().day))

    def filter_age_max(self, queryset, name, value):
        return queryset.filter(birthday__gte=date(date.today().year - value, date.today().month, date.today().day))
