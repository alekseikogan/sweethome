from django import template
from carts.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)


@register.filter
def ru_plural(value):
    '''Определение склонения слова <товар>
    Принимает количество товара'''
    value = int(value)

    if value % 10 == 1 and value % 100 != 11:
        variant = 'товар'
    elif value % 10 >= 2 and value % 10 <= 4 and \
            (value % 100 < 10 or value % 100 >= 20):
        variant = 'товара'
    else:
        variant = 'товаров'

    return variant
