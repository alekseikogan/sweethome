from django.shortcuts import render


def create_order(request):
    '''Создание заказа'''
    return render(request, 'orders/create_order.html')