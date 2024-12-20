from django.urls import path

from .api.Article.ArticleRetrieve.views import ArticleRetrieveAPIView
from .api.Article.ArticleList.views import ArticleListAPIView
from .api.Article.ArticleDestroy.views import ArticleDestroyAPIView
from .api.Article.ArticleCreate.views import ArticleCreateAPIView
from .api.Article.ArticleUpdate.views import ArticleUpdateAPIView


urlpatterns = [
    path('article-retrieve/<slug:slug>/', ArticleRetrieveAPIView.as_view()),
    path('article-list/', ArticleListAPIView.as_view()),
    path('article-destroy/<slug:slug>/', ArticleDestroyAPIView.as_view()),
    path('article-create/', ArticleCreateAPIView.as_view()),
    path('article-update/<slug:slug>/', ArticleUpdateAPIView.as_view()),
]
