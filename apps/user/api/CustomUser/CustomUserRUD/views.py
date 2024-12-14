from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.user.models import CustomUser
from .serializers import CustomUserRUDAPISerializer


class CustomUserRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRUDAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def  get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

custom_user_rud_api_view = CustomUserRUDAPIView.as_view()
