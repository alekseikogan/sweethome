from carts.models import Cart
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegisterForm


def login(request):
    '''Авторизация пользователей'''

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт')

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                # типа челик сидел на logout - зашел и его кидает обратно на выход
                if redirect_page and redirect_page != reverse('users:logout'):
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

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

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

    orders = Order.objects.filter(
        user=request.user).prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('product')
            )
        ).order_by('-id')

    context = {
        'title': 'Личный кабинет',
        'form': form,
        'orders': orders,
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
