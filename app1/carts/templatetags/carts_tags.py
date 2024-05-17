from django import template

from carts.models import Cart

register = template.Library()

@register.simple_tag()
def user_carts(request):
    # Выбираем все корзины этого пользователя
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
