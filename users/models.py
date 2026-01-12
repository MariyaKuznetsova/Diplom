from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    nik = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="Как вас приветствовать?"
    )
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Телефон"
    )
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True)
    country = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Страна"
    )
    city = models.CharField(max_length=20, blank=True, null=True, verbose_name="Город")
    myself = models.TextField(blank=True, null=True, verbose_name="О себе")

    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
