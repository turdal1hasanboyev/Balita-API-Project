from rest_framework import serializers

from apps.category.models import Category


class CategoryLCAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
        