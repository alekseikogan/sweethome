from django.shortcuts import render

from goods.models import Product


def index(request):
    '''Главная страница'''
    featured_products = Product.objects.order_by('?')[:3]

    context = {
        'title': 'Главная страница',
        'content': 'Главная страница SweetHome',
        'featured_products': featured_products,
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    '''Про нас'''
    context = {
        'title': 'О нас',
        'content': 'Про нас',
        'text_on_page': 'SweetHome - это интернет-магазин мебели и декора, который помогает быстро и удобно оформить дом в едином стиле.'
    }
    return render(request, 'main/about.html', context=context)


def delivery_payment(request):
    context = {
        'title': 'Доставка и оплата',
    }
    return render(request, 'main/delivery_payment.html', context=context)


def contacts(request):
    context = {
        'title': 'Контактная информация',
    }
    return render(request, 'main/contacts.html', context=context)
