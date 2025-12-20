from django.urls import path
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
    path("authors/", views.author_list, name="author_list"),
    path("authors/create/", views.author_create, name="author_create"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/create/", views.tag_create, name="tag_create"),
]
