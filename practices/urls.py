from django.urls import path
from practices import views

urlpatterns = [
    path(
        "hello/", views.hello_world, name="hello_world"
    ),  # path(路徑,view的函式名稱,name非必要，在幫url取名，方便收尋且說明)
    path(
        "greeting/",
        views.greeting,
        name="greeting",
    ),
    path("search/", views.search, name="search"),
]
