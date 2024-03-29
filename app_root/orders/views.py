from carts.models import Cart
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from django.contrib.auth.decorators import login_required


@login_required
def create_order(request):
    '''Создание заказа'''

    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # создаем заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        # создаем заказанные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = product.name
                            price = product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе,\
                                                      В наличии - {product.quantity}')

                            # Создаем часть объекта Заказа - товар с опр. количеством
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                            # вычитаем товар из склада (свободный остаток)
                            product.quantity -= quantity
                            product.save()

                        # чистим корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('users:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('carts:order')

    else:
        # сюда кинет впервые - предзаполнит форму Фамилия Имя
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Оформление заказа',
        'form': form,
        'order': True,
    }

    return render(request, 'orders/create_order.html', context=context)
