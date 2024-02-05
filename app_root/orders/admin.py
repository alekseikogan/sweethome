from django.contrib import admin
from orders.models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'name', 'price', 'quantity',)
    search_fields = ('product', 'name',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.Models):

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