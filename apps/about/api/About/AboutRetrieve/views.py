from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import AboutRetrieveAPISerializer
from apps.about.models import About


class AboutRetrieveAPIView(RetrieveAPIView):
    """
    API endpoint that allows users to view about page.
    """
    queryset = About.objects.all()
    serializer_class = AboutRetrieveAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

about_retrieve_api_view = AboutRetrieveAPIView.as_view()
