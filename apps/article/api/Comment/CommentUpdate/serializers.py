from rest_framework import serializers

from apps.article.models import Comment

from apps.user.api.CustomUser.CustomUserLC.serializers import CustomUserLCAPISerializer


class CommentUpdateAPISerializer(serializers.ModelSerializer):
    user = CustomUserLCAPISerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'article',
            'name',
            'email',
            'web_site',
            'comment',
            'is_active',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]
