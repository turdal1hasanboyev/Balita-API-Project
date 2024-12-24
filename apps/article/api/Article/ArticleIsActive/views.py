from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.response import Response

from apps.article.models import Article
from .serializers import ArticleIsActiveAPIViewSerializer


class ArticleIsActiveAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleIsActiveAPIViewSerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
        IsAuthenticatedOrReadOnly
    ]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = not instance.is_active
        instance.save()
        return Response({'message': 'is_active updated', 'is_active': instance.is_active})
        
article_is_active_api_view = ArticleIsActiveAPIView.as_view()
