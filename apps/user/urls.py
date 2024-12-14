from django.urls import path

from .api.CustomUser.CustomUserLC.views import custom_user_lc_api_view
from .api.CustomUser.CustomUserRUD.views import custom_user_rud_api_view


urlpatterns = [
    path('custom_user_lc/', custom_user_lc_api_view, name='custom_user_lc'),
    path('custom_user_rud/<int:pk>/', custom_user_rud_api_view, name='custom_user_rud'),
]
