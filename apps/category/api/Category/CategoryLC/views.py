from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.category.models import Category
from .serializers import CategoryLCAPISerializer
from .filters import CategoryFilter


class CategoryLCAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryLCAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    filterset_class = CategoryFilter
    pagination_class = None

    def  get_queryset(self):
        return Category.objects.filter(is_active=True)

category_lc_api_view = CategoryLCAPIView.as_view()
