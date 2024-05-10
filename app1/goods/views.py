
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products


def catalog(request, category_slug):
    """Передаем category_slug для отображения в адресе slug, например, 
    /catalog/kuhnya/"""
    page = request.GET.get('page', 1)
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3) #  количество товаров,выводимых на странице
    current_page = paginator.page(int(page))
    


    context = {
        "title": "Home - каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    """Передаем product_slug для отображения в адресе slug, например,
    /catalog/product/chajnyj-stolik-i-tri-stula/"""

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, "goods/product.html", context=context)
