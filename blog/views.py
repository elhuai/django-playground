from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Article, Author, Tag
from blog.forms import ArticleForm, AuthorForm, TagForm
from django.contrib import messages
from blog.filters import ArticleFilter, AuthorFilter, TagFilter
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django_filters.views import FilterView


class ArticleListView(FilterView):
    queryset = Article.objects.select_related("author").prefetch_related("tags")
    filterset_class = ArticleFilter
    template_name = "blog/article_list.html"


class ArticleDetailView(DetailView):
    queryset = Article.objects.select_related("author").prefetch_related("tags")
    pk_url_kwarg = "article_id"


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/article_create.html"
    permission_required = "blog.add_article"
    raise_exception = True

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        form.save_m2m()
        messages.success(self.request, f"文章「{self.object.title}」已成功建立。")
        return redirect(self.get_success_url())


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm  #
    template_name = "blog/article_edit.html"
    pk_url_kwarg = "article_id"
    permission_required = "blog.change_article"
    raise_exception = True

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, f"文章「{self.object.title}」已成功更新。")
        return redirect(self.get_success_url())


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "blog/article_delete.html"  # 指定渲染的頁面
    pk_url_kwarg = "article_id"  # 從URL中取得文章ID
    success_url = reverse_lazy("blog:article_list")  # 刪除後重定向的URL
    permission_required = "blog.change_article"
    raise_exception = True

    def form_valid(self, form):  # 覆寫form_valid方法以添加自定義行為讓提示訊息出現
        messages.success(self.request, f"文章「{self.object.title}」已成功刪除。")
        self.object.delete()
        return redirect(self.get_success_url())


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
