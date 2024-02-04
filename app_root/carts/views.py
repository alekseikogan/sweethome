from django.shortcuts import redirect
from carts.models import Cart

from goods.models import Product


def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    pass


def cart_remove(request, cart_id):
    '''Удаление товара из корзины'''
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])
