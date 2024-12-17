from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.category.models import Tag
from .serializers import TagLCAPISerializer
from .filters import TagFilter


class TagLCAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagLCAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    filterset_class = TagFilter

    def  get_queryset(self):
        return Tag.objects.filter(is_active=True)
    