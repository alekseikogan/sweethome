from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import ProfileForm, UserLoginForm, UserRegisterForm


def login(request):
    '''Авторизация пользователей'''

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт')

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def register(request):
    '''Регистрация пользователей'''

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, Вы зарегистрировались и вошли в аккаунт')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form,
    }

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    '''Профиль пользователя'''

    if request.method == 'POST':
        form = ProfileForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Личный кабинет',
        'form': form,
    }

    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    username = request.user.username
    auth.logout(request)
    messages.success(request, f'{username}, Вы вышли из аккаунта')
    return redirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')
