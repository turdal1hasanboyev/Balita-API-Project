from rest_framework import serializers

from apps.user.models import CustomUser


class CustomUserLCAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
