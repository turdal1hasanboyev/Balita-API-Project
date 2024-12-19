from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import AboutUpdateAPISerializer
from apps.about.models import About


class AboutUpdateAPIView(UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUpdateAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

about_update_api_view = AboutUpdateAPIView.as_view()
