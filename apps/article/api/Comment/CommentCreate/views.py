from rest_framework.generics import CreateAPIView

from rest_framework.permissions import IsAuthenticated

from apps.article.models import Comment
from .serializers import CommentCreateAPISerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateAPISerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(is_active=True).select_related('user', 'article')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

comment_create_as_view = CommentCreateAPIView.as_view()
    