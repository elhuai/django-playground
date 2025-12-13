from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Article, Author, Tag
from blog.forms import ArticleForm


def article_list(request):
    # articles = Article.objects.all()
    articles = Article.objects.select_related("author").prefetch_related("tags")
    return render(request, "blog/article_list.html", {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(
        Article.objects.select_related("author").prefetch_related("tags"),
        id=article_id,
    )
    return render(request, "blog/article_detail.html", {"article": article})


def author_list(request):
    authors = Author.objects.all()
    return render(request, "blog/author_list.html", {"authors": authors})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", {"tags": tags})


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("blog:article_detail", article_id=article.id)
    else:
        form = ArticleForm()
    return render(
        request,
        "blog/article_create.html",
        {"form": form},
    )
