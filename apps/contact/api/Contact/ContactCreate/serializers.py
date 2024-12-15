from rest_framework.serializers import ModelSerializer

from apps.contact.models import Contact


class ContactCreateAPISerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'phone_number',
            'email',
            'message',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
