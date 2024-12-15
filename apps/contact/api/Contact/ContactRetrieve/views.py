from rest_framework.generics import RetrieveAPIView

from .serializers import ContactRetrieveAPISerializer
from apps.contact.models import Contact


class ContactRetrieveAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactRetrieveAPISerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
