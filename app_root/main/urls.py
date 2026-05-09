from django.urls import path

from main.views import about, contacts, delivery_payment, index

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('delivery-payment/', delivery_payment, name='delivery_payment'),
    path('contacts/', contacts, name='contacts'),
]
