from rest_framework.serializers import ModelSerializer

from apps.article.models import Article


class ArticleForBannerAPIViewSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['for_banner']
