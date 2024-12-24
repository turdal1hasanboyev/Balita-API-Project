from rest_framework.generics import RetrieveAPIView

from rest_framework.permissions import IsAuthenticated

from apps.article.models import Comment
from .serializers import CommentRetrieveAPISerializer


class CommentRetrieveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'article')

comment_retrieve_as_view = CommentRetrieveAPIView.as_view()
    