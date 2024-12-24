from rest_framework.serializers import ModelSerializer

from apps.article.models import Comment
from apps.user.api.CustomUser.CustomUserLC.serializers import CustomUserLCAPISerializer
from apps.article.api.Article.ArticleRetrieve.serializers import ArticleRetrieveAPISerializer


class CommentListAPISerializer(ModelSerializer):
    user = CustomUserLCAPISerializer(read_only=True)
    article = ArticleRetrieveAPISerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
