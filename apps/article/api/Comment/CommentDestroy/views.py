from rest_framework.generics import DestroyAPIView

from rest_framework.permissions import IsAuthenticated

from apps.article.models import Comment
from .serializers import CommentDestroyAPISerializer


class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroyAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'article')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
    