from rest_framework.serializers import ModelSerializer

from apps.common.models import Subscribe


class SubscribeRUDAPISerializer(ModelSerializer):
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

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
