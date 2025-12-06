from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("practices/", include("practices.urls")),
    path("blog/", include("blog.urls")),
]
