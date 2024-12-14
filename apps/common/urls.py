from django.urls import path

from .api.Subscribe.SubscribeLC.views import SubscribeLCAPIView
from .api.Subscribe.SubscribeRUD.views import SubscribeRUDAPIView


urlpatterns = [
    path('subscribe_lc/', SubscribeLCAPIView.as_view(), name='subscribe_lc'),
    path('subscribe_rud/<int:pk>/', SubscribeRUDAPIView.as_view(), name='subscribe_rud'),
]
