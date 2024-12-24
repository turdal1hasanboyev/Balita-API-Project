from rest_framework import serializers

from apps.article.models import Comment


class CommentIsActiveAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['is_active']
