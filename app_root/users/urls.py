from django.urls import path

from users.views import login, register, profile, logout, users_cart

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('users-cart/', users_cart, name='users_cart'),
]
