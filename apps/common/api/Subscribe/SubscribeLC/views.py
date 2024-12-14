from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.common.models import Subscribe
from .serializers import SubscribeLCAPISerializer
from .filters import SubscribeFilterSet


class SubscribeLCAPIView(ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeLCAPISerializer
    permission_classes = [IsAuthenticated]
    filterset_class = SubscribeFilterSet
    pagination_class = None

    def get_queryset(self):
        return Subscribe.objects.filter(is_active=True)
