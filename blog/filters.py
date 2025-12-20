import django_filters

from blog.models import Article, Author, Tag


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {
            "title": ["icontains"],
            "author": ["exact"],
            "tags": ["exact"],
        }


class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            "name": ["icontains"],
            "email": ["contains"],
            "bio": ["exact"],
        }


class TagFilter(django_filters.FilterSet):
    class Meta:
        model = Tag
        fields = {
            "name": ["icontains"],
        }
