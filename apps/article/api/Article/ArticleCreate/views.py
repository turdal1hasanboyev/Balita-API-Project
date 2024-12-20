from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import ArticleCreateAPISerializer
from apps.article.models import Article


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('tags')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        