from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from blog.models import Article, Author
from blog.serializers import ArticleSerializer, AuthorSerializer


class ArticleViewSet(ModelViewSet):
    """文章 API ViewSet"""

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "title"]
    filterset_fields = ["is_published", "author"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AuthorViewSet(mixins.DestroyModelMixin, ReadOnlyModelViewSet):
    """作者 API ViewSet"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
