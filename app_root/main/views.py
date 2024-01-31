from django.shortcuts import render

from goods.models import Category, Product


def index(request):
    '''Главная страница'''
    categories = Category.objects.all()
    context = {
        'title': 'Главная страница',
        'content': 'Главная страница SweetHome',
        'categories': categories,
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    '''Про нас'''
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context=context)
