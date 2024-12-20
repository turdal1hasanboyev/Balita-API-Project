from rest_framework.serializers import ModelSerializer

from apps.article.models import Article

from apps.user.api.CustomUser.CustomUserLC.serializers import CustomUserLCAPISerializer
from apps.category.api.Category.CategoryLC.serializers import CategoryLCAPISerializer
from apps.category.api.Tag.TagLC.serializers import TagLCAPISerializer


class ArticleListAPISerializer(ModelSerializer):
    author = CustomUserLCAPISerializer(read_only=True)
    category = CategoryLCAPISerializer(read_only=True)
    tags = TagLCAPISerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
