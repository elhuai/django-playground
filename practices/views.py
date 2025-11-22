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
