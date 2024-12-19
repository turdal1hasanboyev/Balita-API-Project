from django.urls import path

from .api.About.AboutCreate.views import about_create_api_view
from .api.About.AboutList.views import about_list_api_view
from .api.About.AboutDestroy.views import about_destroy_api_view
from .api.About.AboutRetrieve.views import about_retrieve_api_view
from .api.About.AboutUpdate.views import about_update_api_view

# test view
from .api.About.AboutIsActive.views import about_is_active_api_view


urlpatterns = [
    path('about-create/', about_create_api_view, name='about-create-api-view'),
    path('about-list/', about_list_api_view, name='about-list-api-view'),
    path('about-destroy/<int:pk>/', about_destroy_api_view, name='about-destroy-api-view'),
    path('about-retrieve/<int:pk>/', about_retrieve_api_view, name='about-retrieve-api-view'),
    path('about-update/<int:pk>/', about_update_api_view, name='about-update-api-view'),

    # test
    path('about-is-active/<int:pk>/', about_is_active_api_view, name='about-is-active-api-view'),
]
