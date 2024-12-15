from rest_framework.serializers import ModelSerializer

from apps.contact.models import Contact


class ContactRetrieveAPISerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
