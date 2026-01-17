from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import mixins

from blog.models import Article, Author
from blog.serializers import ArticleSerializer, AuthorSerializer


class ArticleViewSet(ModelViewSet):
    """文章 API ViewSet"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AuthorViewSet(mixins.DestroyModelMixin, ReadOnlyModelViewSet):
    """作者 API ViewSet"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
