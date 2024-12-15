from rest_framework.generics import UpdateAPIView

from .serializers import ContactUpdateAPISerializer
from apps.contact.models import Contact


class ContactUpdateAPIView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUpdateAPISerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Contact.objects.filter(is_active=True)
