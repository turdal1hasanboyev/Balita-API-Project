from django.urls import path

from .api.Contact.ContactRetrieve.views import ContactRetrieveAPIView
from .api.Contact.ContactList.views import ContactListAPIView
from .api.Contact.ContactDestroy.views import ContactDestroyAPIView
from .api.Contact.ContactUpdate.views import ContactUpdateAPIView
from .api.Contact.ContactCreate.views import ContactCreateAPIView


urlpatterns = [
    path('contact_retrieve/<int:pk>/', ContactRetrieveAPIView.as_view(), name='contact_retrieve'),
    path('contact_list/', ContactListAPIView.as_view(), name='contact_list'),
    path('contact_create/', ContactCreateAPIView.as_view(), name='contact_create'),
    path('contact_destroy/<int:pk>/', ContactDestroyAPIView.as_view(), name='contact_destroy'),
    path('contact_update/<int:pk>/', ContactUpdateAPIView.as_view(), name='contact_update'),
]
