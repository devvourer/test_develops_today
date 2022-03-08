from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .tasks import upvote_article


class ArticleViewSet(ModelViewSet):
    model = Article
    queryset = Article.objects.with_comments_count()
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
    serializer_class = ArticleSerializer

    @action(methods=["post"], permission_classes=[IsAuthenticated], detail=True)
    def upvote(self, request, pk=None):
        upvote_article.delay(pk)
        return Response(status=status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
    serializer_class = CommentSerializer
