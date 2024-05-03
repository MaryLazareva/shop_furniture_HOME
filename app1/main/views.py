from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        "title": "Home - главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - о нас",
        "content": "О нас",
        "text_on_page": "Текст о магазине",
    }
    return render(request, "main/about.html", context)
