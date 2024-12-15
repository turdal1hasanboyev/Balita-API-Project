from rest_framework.serializers import ModelSerializer

from apps.contact.models import Contact


class ContactDestroyAPISerializer(ModelSerializer):
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
