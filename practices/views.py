from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return render(request, "practices/hello.html")


def greeting(request):
    content = "Djang12345"
    return render(request, "practices/greeting.html", {"content": content})


def search(request):
    keyword = request.GET.get("q", "")
    return HttpResponse(f"Keyword: {keyword}")


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
