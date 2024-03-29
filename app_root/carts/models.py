from django.db import models
from goods.models import Product
from users.models import User


class CartQueryset(models.QuerySet):

    def total_price(self):
        '''Подсчет общей стоимости товаров в корзине'''
        return sum([cart.products_price() for cart in self])

    def total_quantity(self):
        '''Подсчет общего количества товаров в корзине'''
        if self:
            return sum([cart.quantity for cart in self])
        return 0


class Cart(models.Model):

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт')

    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество')

    session_key = models.CharField(
        max_length=32,
        null=True,
        blank=True)

    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    objects = CartQueryset().as_manager()

    def products_price(self):
        '''Стоимость конкретного товара с учетом количества'''
        return round(self.product.sell_price()*self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'
