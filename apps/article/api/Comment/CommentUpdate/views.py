from rest_framework.generics import UpdateAPIView

from rest_framework.permissions import IsAuthenticated

from apps.article.models import Comment
from .serializers import CommentUpdateAPISerializer


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'article')
    
    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user.id)

comment_update_as_view = CommentUpdateAPIView.as_view()
    