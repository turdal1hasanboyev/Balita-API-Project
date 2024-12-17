from rest_framework import serializers

from apps.category.models import Tag


class TagRUDAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
