from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Article, Author, Tag
from blog.forms import ArticleForm, AuthorForm, TagForm
from django.utils import timezone
from django.contrib import messages
from blog.filters import ArticleFilter, AuthorFilter, TagFilter
from django.contrib.auth.decorators import login_required


def article_list(request):
    filter_ = ArticleFilter(
        request.GET or None,
        queryset=Article.objects.filter(is_deleted=False)
        .select_related("author")
        .prefetch_related("tags"),
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


@login_required
def article_create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.created_by = request.user
        article.save()
        messages.success(request, f"文章「{article.title}」已成功建立。")
        return redirect("blog:article_detail", article_id=article.id)
    return render(request, "blog/article_create.html", {"form": form})


@login_required
def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save()
        messages.success(request, f"文章「{article.title}」已成功更新。")
        return redirect("blog:article_detail", article_id=article.id)

    return render(request, "blog/article_edit.html", {"form": form, "article": article})


@login_required
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.is_deleted = True
        article.deleted_at = timezone.now()
        article.save()  # 不是 delete()！
        messages.success(request, f"文章「{article.title}」已成功刪除。")
        return redirect("blog:article_list")
    return render(request, "blog/article_delete.html", {"article": article})


def article_bulk_delete(request):
    if request.method == "POST":
        article_ids = request.POST.getlist("article_ids")
        if article_ids:
            deleted_count, _ = Article.objects.filter(id__in=article_ids).delete()
            messages.success(request, f"已成功刪除 {deleted_count} 篇文章")
        else:
            messages.warning(request, "請先選取至少一個要刪除的文章")

    return redirect("blog:article_list")


def author_list(request):
    author_filter = AuthorFilter(
        request.GET or None,
        queryset=Author.objects.prefetch_related("articles"),
    )
    return render(request, "blog/author_list.html", {"filter": author_filter})


def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        author = form.save()
        messages.success(request, f"作者「{author.name}」已成功建立。")
        return redirect("blog:author_list")
    return render(request, "blog/author_create.html", {"form": form})


def author_detail(request, author_id):
    author = get_object_or_404(
        Author.objects.prefetch_related("articles"),
        id=author_id,
    )
    return render(request, "blog/author_detail.html", {"author": author})


def tag_list(request):
    tags_filter = TagFilter(
        request.GET or None,
        queryset=Tag.objects.prefetch_related("articles"),
    )
    return render(request, "blog/tag_list.html", {"filter": tags_filter})


def tag_create(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        tag = form.save()
        messages.success(request, f"標籤「{tag.name}」已成功建立。")
        return redirect("blog:tag_list")
    return render(request, "blog/tag_create.html", {"form": form})
