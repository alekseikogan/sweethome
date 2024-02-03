from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(
        upload_to='users_image',
        verbose_name='Аватар',
        blank=True,
        null=True)

    class Meta:
        db_table = 'user_custom'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
