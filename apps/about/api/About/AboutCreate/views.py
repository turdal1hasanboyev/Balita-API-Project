from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import AboutCreateAPISerializer
from apps.about.models import About


class AboutCreateAPIView(CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutCreateAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

about_create_api_view = AboutCreateAPIView.as_view()
