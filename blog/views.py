from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from blog.filters import ArticleFilter, AuthorFilter, TagFilter
from blog.forms import ArticleForm, AuthorForm, TagForm
from blog.models import Article, Author, Tag


class ArticleListView(FilterView):
    queryset = Article.objects.select_related("author").prefetch_related("tags")
    filterset_class = ArticleFilter
    template_name = "blog/article_list.html"


class ArticleDetailView(DetailView):
    queryset = Article.objects.select_related("author").prefetch_related("tags")
    pk_url_kwarg = "article_id"


class ArticleCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/article_create.html"
    permission_required = "blog.add_article"
    raise_exception = True
    success_message = _("文章「%(title)s」已成功建立。")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/article_edit.html"
    pk_url_kwarg = "article_id"
    permission_required = "blog.change_article"
    raise_exception = True
    success_message = _("文章「%(title)s」已成功更新。")


class ArticleDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Article
    template_name = "blog/article_delete.html"
    pk_url_kwarg = "article_id"
    success_url = reverse_lazy("blog:article_list")
    permission_required = "blog.delete_article"
    raise_exception = True

    def get_success_message(self, cleaned_data):
        return gettext("文章「%(title)s」已成功刪除。") % {"title": self.object.title}


@permission_required("blog.delete_article", raise_exception=True)
def article_bulk_delete(request):
    if request.method == "POST":
        article_ids = request.POST.getlist("article_ids")
        if article_ids:
            deleted_count, _ = Article.objects.filter(id__in=article_ids).delete()
            messages.success(request, gettext("已成功刪除 %(count)d 篇文章") % {"count": deleted_count})
        else:
            messages.warning(request, _("請先選取至少一個要刪除的文章"))

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
        messages.success(request, _("作者「%(name)s」已成功建立。") % {"name": author.name})
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
        messages.success(request, _("標籤「%(name)s」已成功建立。") % {"name": tag.name})
        return redirect("blog:tag_list")
    return render(request, "blog/tag_create.html", {"form": form})
