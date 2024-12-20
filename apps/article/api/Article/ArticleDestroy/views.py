from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import ArticleDestroyAPISerializer
from apps.article.models import Article


class ArticleDestroyAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDestroyAPISerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticatedOrReadOnly,
    ]
    lookup_field = 'slug'

    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('tags')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
