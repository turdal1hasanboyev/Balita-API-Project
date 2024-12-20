from rest_framework.generics import ListAPIView

from .serializers import ArticleListAPISerializer
from apps.article.models import Article
from .filters import ArticleFilter


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListAPISerializer
    filterset_class = ArticleFilter

    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('tags')
    