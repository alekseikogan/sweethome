from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Главная страница SweetHome'
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('about')
