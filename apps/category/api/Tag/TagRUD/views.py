from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.category.models import Tag
from .serializers import TagRUDAPISerializer


class TagRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagRUDAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def  get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
