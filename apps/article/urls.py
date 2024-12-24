from django.urls import path

from .api.Article.ArticleRetrieve.views import ArticleRetrieveAPIView
from .api.Article.ArticleList.views import ArticleListAPIView
from .api.Article.ArticleDestroy.views import ArticleDestroyAPIView
from .api.Article.ArticleCreate.views import ArticleCreateAPIView
from .api.Article.ArticleUpdate.views import ArticleUpdateAPIView

from .api.Article.ArticleIsActive.views import article_is_active_api_view
from .api.Article.ArticleForBanner.views import article_for_banner_api_view

from .api.Comment.CommentCreate.views import comment_create_as_view
from .api.Comment.CommentRetrieve.views import comment_retrieve_as_view
from .api.Comment.CommentList.views import comment_list_as_view
from .api.Comment.CommentDestroy.views import CommentDestroyAPIView
from .api.Comment.CommentUpdate.views import comment_update_as_view

from .api.Comment.CommentIsActive.views import comment_is_active_as_view


urlpatterns = [
    path('article-retrieve/<slug:slug>/', ArticleRetrieveAPIView.as_view()),
    path('article-list/', ArticleListAPIView.as_view()),
    path('article-destroy/<slug:slug>/', ArticleDestroyAPIView.as_view()),
    path('article-create/', ArticleCreateAPIView.as_view()),
    path('article-update/<slug:slug>/', ArticleUpdateAPIView.as_view()),

    path('article-is-active/<int:pk>/', article_is_active_api_view),
    path('article-for-banner/<int:pk>/', article_for_banner_api_view),

    path('comment-create/', comment_create_as_view, name='comment-create'),
    path('comment-retrieve/<int:pk>/', comment_retrieve_as_view, name='comment-retrieve'),
    path('comment-list/', comment_list_as_view, name='comment-list'),
    path('comment-destroy/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment-destroy'),
    path('comment-update/<int:pk>/', comment_update_as_view, name='comment-update'),
    path('comment-is-active/<int:pk>/', comment_is_active_as_view, name='comment-is-active'),
]
