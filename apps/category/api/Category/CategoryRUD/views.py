from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.category.models import Category
from .serializers import CategoryRUDAPISerializer


class CategoryRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRUDAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def  get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

category_rud_api_view = CategoryRUDAPIView.as_view()
