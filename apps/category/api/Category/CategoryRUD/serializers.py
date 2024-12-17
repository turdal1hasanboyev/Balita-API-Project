from rest_framework import serializers

from apps.category.models import Category


class CategoryRUDAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
