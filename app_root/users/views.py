from django.shortcuts import render


def login(request):
    '''Авторизация пользователей'''
    context = {
        'title': 'Авторизация'
    }

    return render(request, 'users/login.html', context)


def register(request):
    '''Регистрация пользователей'''
    context = {
        'title': 'Регистрация'
    }

    return render(request, 'users/register.html', context)


def profile(request):
    '''Профиль пользователя'''
    context = {
        'title': 'Личный кабинет'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    return render(request, '')
