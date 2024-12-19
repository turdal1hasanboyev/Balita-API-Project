from rest_framework import serializers

from apps.about.models import About


class AboutIsActiveAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['is_active']  # Faqat is_active maydonini ko'rsatamiz
