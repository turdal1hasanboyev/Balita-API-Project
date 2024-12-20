import django_filters

from apps.article.models import Article
from apps.category.models import Category
from apps.category.models import Tag


class ArticleFilter(django_filters.FilterSet):
    # Filtrlash uchun kerakli maydonlarni belgilaymiz
    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all())
    is_active = django_filters.BooleanFilter(field_name='is_active')  # is_active maydoni filtri
    for_banner = django_filters.BooleanFilter()  # Banner uchun flag
    
    class Meta:
        model = Article
        fields = ['name', 'category', 'tags', 'is_active', 'for_banner']
