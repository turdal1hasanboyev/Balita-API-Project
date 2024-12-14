from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import SubscribeRUDAPISerializer
from apps.common.models import Subscribe


class SubscribeRUDAPIView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to view, edit or delete their own subscribe instances.
    """
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeRUDAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
