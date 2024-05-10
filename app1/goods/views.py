
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_list_or_404, render

from goods.utils import q_search
from goods.models import Products


def catalog(request, category_slug=None):
    """Передаем category_slug для отображения в адресе slug, например, 
    /catalog/kuhnya/"""
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    
    # Фильтрация по категориям
    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)   
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404("No Products found matching the category.")


    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)


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
