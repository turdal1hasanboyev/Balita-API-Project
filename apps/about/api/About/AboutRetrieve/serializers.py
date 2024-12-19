from rest_framework.serializers import ModelSerializer

from ....models import About


class AboutRetrieveAPISerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
