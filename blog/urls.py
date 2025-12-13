from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("articles/", views.article_list, name="article_list"),
    path("articles/<int:article_id>/", views.article_detail, name="article_detail"),
    path("authors/", views.author_list, name="author_list"),
    path("tags/", views.tag_list, name="tag_list"),
]
