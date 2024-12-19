from rest_framework.serializers import ModelSerializer

from apps.about.models import About


class AboutDestroyAPISerializer(ModelSerializer):
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
