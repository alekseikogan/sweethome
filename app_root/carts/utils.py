from carts.models import Cart


def get_user_carts(request):
    '''Получает все корзины пользователя'''
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
