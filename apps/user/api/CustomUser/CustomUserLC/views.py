from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.user.models import CustomUser
from .serializers import CustomUserLCAPISerializer
from .filters import CustomUserFilterSet


class CustomUserLCAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserLCAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    filterset_class = CustomUserFilterSet
    pagination_class = None

    def  get_queryset(self):
        return self.queryset.filter(is_active=True)

custom_user_lc_api_view = CustomUserLCAPIView.as_view()
