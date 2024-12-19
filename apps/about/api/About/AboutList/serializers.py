from rest_framework.serializers import ModelSerializer

from apps.about.models import About


class AboutListAPISerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
