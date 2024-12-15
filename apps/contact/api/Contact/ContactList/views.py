from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import ContactListAPISerializer
from apps.contact.models import Contact
from .filters import ContactFilter


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListAPISerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    filterset_class = ContactFilter

    def get_queryset(self):
        return Contact.objects.filter(is_active=True)
