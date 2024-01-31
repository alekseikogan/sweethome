from django.shortcuts import render


def catalog(request):
    '''Каталог товаров - главная'''
    context = {
        'title': 'Каталог',
        'goods': 'hello'
    }
    return render(request, 'goods/catalog.html', context=context)


def product(request):
    '''Карточка товара'''
    context = {
        'title': 'Товар',
        'content': 'Карточка товара'
    }
    return render(request, 'goods/product.html', context=context)