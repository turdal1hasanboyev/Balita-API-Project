from rest_framework.generics import CreateAPIView

from .serializers import ContactCreateAPISerializer
from apps.contact.models import Contact


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateAPISerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
