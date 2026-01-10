from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return render(request, "practices/hello.html")


def greeting(request):
    content = "Djang12345"
    return render(request, "practices/greeting.html", {"content": content})


def search(request):
    keyword = request.GET.get("keyword", "")
    return render(request, "practices/search.html", {"keyword": keyword})


def product_list(request):
    category = request.GET.get("category", "all")
    sort = request.GET.get("sort", "newest")
    page = request.GET.get("page", "1")
    return HttpResponse(f"分類: {category}, 排序: {sort}, 頁數: {page}")


def personal_info(request):
    name = request.GET.get("name", "Django")
    age = request.GET.get("age", "10")
    gender = request.GET.get("gender", "male")
    return HttpResponse(f"性名: {name}, 年紀: {age}, 性別: {gender}")


def filter_products(request):
    colors = request.GET.getlist("color")
    return HttpResponse(f"選擇的顏色: {', '.join(colors)}")


def product_amount(request, number):
    return HttpResponse(f"商品數量:, {number}個")


def product_manufacturing_date(request, year, month, product_content):
    return HttpResponse(f"製造日期: {year} 年 {month} 月 - {product_content}")


def user_articles(request, username):  # username是必填，sort page不填就走預設
    sort = request.GET.get("sort", "newest")
    page = request.GET.get("page", "1")
    return HttpResponse(f"{username} 的文章, 排序: {sort}, 頁數: {page}")


def advanced_search(request):
    keyword = request.GET.get("q", "")
    category = request.GET.get("category", "all")
    sort = request.GET.get("sort", "newest")
    size = request.GET.get("size", "newest")
    return render(
        request,
        "practices/advanced_search.html",
        {"keyword": keyword, "category": category, "sort": sort, "size": size},
    )


def color_filter(request):
    colors = request.GET.getlist("color")
    return render(
        request,
        "practices/color_filter.html",
        {"colors": colors},
    )


def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")
        context = {
            "success": True,  # 一定要加這條
            "name": name,
            "email": email,
            "message": message,
        }
    return render(request, "practices/contact.html", context)


def cookie_counter(request):
    # 從 Cookie 讀取訪問次數
    visit_count = request.COOKIES.get("visit_count", "0")
    visit_count = int(visit_count) + 1

    # 建立回應
    response = HttpResponse(f"你已經訪問了 {visit_count} 次")

    # 設定 Cookie
    response.set_cookie("visit_count", str(visit_count))

    return response


def theme_preference(request):
    # 從 GET 參數讀取主題設定
    theme = request.GET.get("theme")

    # 從 Cookie 讀取目前的主題
    current_theme = request.COOKIES.get("theme", "light")

    # 如果有新的主題設定就更新
    if theme:
        current_theme = theme

    # 建立回應
    response = render(request, "practices/theme.html", {"theme": current_theme})

    # 儲存主題設定到 Cookie
    if theme:
        response.set_cookie("theme", current_theme, max_age=7 * 24 * 60 * 60)

    return response
