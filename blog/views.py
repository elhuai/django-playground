from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Article, Author, Tag
from blog.forms import ArticleForm
from django.utils import timezone
from django.contrib import messages
from blog.filters import ArticleFilter


def article_list(request):
    filter_ = ArticleFilter(
        request.GET or None,
        queryset=Article.objects.select_related("author").prefetch_related("tags"),
    )  # filter 有一個內建function所以刻意加上底線 filter_ 來命名
    return render(
        request, "blog/article_list.html", {"filter": filter_}
    )  # filter_資料以filter名稱傳到前端的時候就轉為filter


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
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save()
        messages.success(request, f"文章「{article.title}」已成功建立。")
        return redirect("blog:article_detail", article_id=article.id)
    return render(request, "blog/article_create.html", {"form": form})


def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        article = form.save()
        messages.success(request, f"文章「{article.title}」已成功更新。")
        return redirect("blog:article_detail", article_id=article.id)

    return render(request, "blog/article_edit.html", {"form": form, "article": article})


def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.is_deleted = True
        article.deleted_at = timezone.now()
        article.save()  # 不是 delete()！
        messages.success(request, f"文章「{article.title}」已成功刪除。")
        return redirect("blog:article_list")
    return render(request, "blog/article_delete.html", {"article": article})
