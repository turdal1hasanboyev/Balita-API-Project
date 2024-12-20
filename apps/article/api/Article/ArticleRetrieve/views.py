from rest_framework.generics import RetrieveAPIView

from .serializers import ArticleRetrieveAPISerializer
from apps.article.models import Article


class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleRetrieveAPISerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author', 'category').prefetch_related('tags')
