from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views

app_name = "blog"
urlpatterns = [
    path("articles/", views.article_list, name="article_list"),
    path("articles/<int:article_id>/", views.article_detail, name="article_detail"),
    path("articles/create/", views.article_create, name="article_create"),
    path("articles/<int:article_id>/edit/", views.article_edit, name="article_edit"),
    path(
        "articles/<int:article_id>/delete/", views.article_delete, name="article_delete"
    ),
    path(
        "articles/bulk-delete/", views.article_bulk_delete, name="article_bulk_delete"
    ),
    path("authors/", views.author_list, name="author_list"),
    path("authors/create/", views.author_create, name="author_create"),
    path("authors/<int:author_id>/", views.author_detail, name="author_detail"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/create/", views.tag_create, name="tag_create"),
]


if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
        *debug_toolbar_urls(),
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
