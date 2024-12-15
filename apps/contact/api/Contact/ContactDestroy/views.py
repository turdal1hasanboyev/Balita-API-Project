from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import ContactDestroyAPISerializer
from apps.contact.models import Contact


class ContactDestroyAPIView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDestroyAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        return Contact.objects.filter(is_active=True)
