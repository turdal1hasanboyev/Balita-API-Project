from rest_framework.serializers import ModelSerializer

from apps.common.models import Subscribe


class SubscribeLCAPISerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = [
            'id',
            'email',
            'url',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
