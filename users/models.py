from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}

class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', unique=True)
    email = models.EmailField(verbose_name='Почта', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    avatar = models.ImageField(upload_to="media/avatar/", verbose_name="Фото", **NULLABLE)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone
