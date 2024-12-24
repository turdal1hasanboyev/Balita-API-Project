from rest_framework import serializers

from apps.article.models import Article


class ArticleIsActiveAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['is_active']
