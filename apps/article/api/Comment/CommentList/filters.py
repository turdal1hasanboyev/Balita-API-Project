from django_filters import rest_framework as filters

from apps.article.models import Comment


class CommentFilter(filters.FilterSet):
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    web_site = filters.CharFilter(field_name='web_site', lookup_expr='icontains')
    comment = filters.CharFilter(field_name='comment', lookup_expr='icontains')

    class Meta:
        model = Comment
        fields = ['is_active', 'created_at', 'name', 'email', 'web_site', 'comment', 'article', 'user']
