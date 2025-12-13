from django.shortcuts import get_object_or_404, render
from blog.models import Article, Author, Tag


def article_list(request):
    articles = Article.objects.select_related("author").all()
    return render(request, "blog/article_list.html", {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "blog/article_detail.html", {"article": article})


def author_list(request):
    authors = Author.objects.all()
    return render(request, "blog/author_list.html", {"authors": authors})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", {"tags": tags})
