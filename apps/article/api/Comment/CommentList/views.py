from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAuthenticated

from apps.article.models import Comment
from .serializers import CommentListAPISerializer
from .filters import CommentFilter


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListAPISerializer
    permission_classes = [IsAuthenticated]
    filterset_class = CommentFilter

    def get_queryset(self):
        return Comment.objects.filter(is_active=True).select_related('user', 'article')

comment_list_as_view = CommentListAPIView.as_view()
    