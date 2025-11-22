from django.urls import path
from practices.views import hello_world

urlpatterns = [
    path(
        "hello/", hello_world, name="hello_world"
    ),  # path(路徑,view的函式名稱,name非必要，在幫url取名，方便收尋且說明)
]
