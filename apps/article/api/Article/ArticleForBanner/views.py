from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.response import Response

from apps.article.models import Article
from .serializers import ArticleForBannerAPIViewSerializer


class ArticleForBannerAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleForBannerAPIViewSerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
        IsAuthenticatedOrReadOnly
    ]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.for_banner = not instance.for_banner
        instance.save()
        return Response({'message': 'for_banner updated', 'for_banner': instance.for_banner})
        
article_for_banner_api_view = ArticleForBannerAPIView.as_view()
