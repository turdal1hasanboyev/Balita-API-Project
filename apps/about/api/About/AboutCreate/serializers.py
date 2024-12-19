from rest_framework import serializers

from apps.about.models import About


class AboutCreateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = [
            'id',
            'name',
            'image',
            'description_1',
            'description_2',
            "description_3",
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'id': {'read_only': True},
        }
