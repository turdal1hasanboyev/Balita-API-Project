from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from apps.about.models import About
from .serializers import AboutIsActiveAPIViewSerializer


class AboutActiveAPIView(UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutIsActiveAPIViewSerializer
    permission_classes = [IsAuthenticated]  # Minimal permissionlar

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()  # PK bo'yicha obyektni oladi
        instance.is_active = not instance.is_active
        instance.save()
        return Response({'message': 'is_active updated', 'is_active': instance.is_active})
        
about_is_active_api_view = AboutActiveAPIView.as_view()
