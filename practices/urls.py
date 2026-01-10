from django.urls import path
from practices import views

app_name = "practices"
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
    path("products/", views.product_list, name="product_list"),
    path("personal_info/", views.personal_info, name="personal_info"),
    path("products/filter/", views.filter_products, name="product_filter"),
    path("products/amount/<int:number>/", views.product_amount, name="product_amount"),
    path(
        "products/manufacturing/date/<int:year>/<int:month>/<slug:product_content>/",
        views.product_manufacturing_date,
        name="product_manufacturing_date",
    ),
    path(
        "users/<str:username>/articles/",
        views.user_articles,
        name="user_articles",
    ),
    path("advanced-search/", views.advanced_search, name="advanced_search"),
    path("color-filter/", views.color_filter, name="color_filter"),
    path("contact/", views.contact, name="contact"),
    path("cookie-counter/", views.cookie_counter, name="cookie_counter"),
    path("theme/", views.theme_preference, name="theme_preference"),
]
