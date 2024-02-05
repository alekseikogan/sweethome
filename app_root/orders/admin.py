from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemTabularAdmin(admin.TabularInline):
    '''Табуляр для OrderAdmin'''
    model = OrderItem
    fields = ('product', 'name', 'price', 'quantity',)
    search_fields = ('product', 'name',)
    extra = 0


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Заказанные продукты в OrderAdmin'''
    list_display = ('order', 'product', 'name', 'price', 'quantity',)
    search_fields = (
        'order',
        'product',
        'name',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Заказы глобально'''

    list_display = (
        'id',
        'user',
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',)

    list_filter = (
        'id',
        'created_timestamp',)

    readonly_fields = ('created_timestamp',)
    inlines = (OrderItemTabularAdmin, )
