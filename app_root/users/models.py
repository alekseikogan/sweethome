from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(
        upload_to='users_image',
        verbose_name='Аватар',
        blank=True,
        null=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True)

    class Meta:
        db_table = 'user_custom'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
