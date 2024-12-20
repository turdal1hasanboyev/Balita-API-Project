from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import ArticleUpdateAPISerializer
from apps.article.models import Article


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleUpdateAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('category', 'author').prefetch_related("tags")
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
