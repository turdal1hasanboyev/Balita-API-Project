from rest_framework import serializers

from apps.category.models import Tag


class TagLCAPISerializer(serializers.ModelSerializer):
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
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
        