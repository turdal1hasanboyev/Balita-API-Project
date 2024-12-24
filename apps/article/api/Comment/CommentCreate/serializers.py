from rest_framework.serializers import ModelSerializer

from apps.article.models import Comment
from apps.user.api.CustomUser.CustomUserLC.serializers import CustomUserLCAPISerializer


class CommentCreateAPISerializer(ModelSerializer):
    user = CustomUserLCAPISerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'article',
            'user',
            'name',
            'email',
            'web_site',
            'comment',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'is_active': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
