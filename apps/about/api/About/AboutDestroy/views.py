from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import AboutDestroyAPISerializer
from apps.about.models import About


class AboutDestroyAPIView(DestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutDestroyAPISerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticatedOrReadOnly,
        IsAuthenticated,
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        return About.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

about_destroy_api_view = AboutDestroyAPIView.as_view()
