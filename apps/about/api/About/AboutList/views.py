from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import AboutListAPISerializer
from apps.about.models import About
from .filters import AboutFilter


class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutListAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    filterset_class = AboutFilter
    pagination_class = None

    def get_queryset(self):
        return About.objects.filter(is_active=True)

about_list_api_view = AboutListAPIView.as_view()
