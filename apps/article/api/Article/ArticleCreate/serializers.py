from rest_framework import serializers

from apps.article.models import Article

from apps.user.api.CustomUser.CustomUserLC.serializers import CustomUserLCAPISerializer


class ArticleCreateAPISerializer(serializers.ModelSerializer):
    author = CustomUserLCAPISerializer(read_only=True)
    
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

        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'id': {'read_only': True},
        }
