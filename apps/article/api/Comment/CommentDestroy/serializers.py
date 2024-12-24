from rest_framework import serializers

from apps.article.models import Comment


class CommentDestroyAPISerializer(serializers.ModelSerializer):
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
