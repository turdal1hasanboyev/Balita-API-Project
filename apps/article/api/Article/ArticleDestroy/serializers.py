from rest_framework.serializers import ModelSerializer

from apps.article.models import Article


class ArticleDestroyAPISerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'slug',
            'image_1',
            'image_2',
            'image_3',
            'description_1',
            'description_2',
            "description_3",
            'author',
            'category',
            'tags',
            'views',
            'for_banner',
            'is_active',
            'created_at',
            'updated_at',
        ]
