from django.urls import path

from .api.Category.CategoryLC.views import category_lc_api_view
from .api.Category.CategoryRUD.views import category_rud_api_view

from .api.Tag.TagLC.views import TagLCAPIView
from .api.Tag.TagRUD.views import TagRUDAPIView


urlpatterns = [
    path('category_lc/', category_lc_api_view, name='category_lc_api_view'),
    path('category_rud/<slug:slug>/', category_rud_api_view, name='category_rud_api_view'),

    path('tag_lc/', TagLCAPIView.as_view(), name='tag_lc_api_view'),
    path('tag_rud/<slug:slug>/', TagRUDAPIView.as_view(), name='tag_rud_api_view'),
]
