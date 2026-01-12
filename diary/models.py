from django.db import models

from users.models import User


class Record(models.Model):
    """Модель записи в дневник"""
    date = models.DateField(verbose_name="Дата записи")
    contents = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Изображение")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец дневника",
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["date", "contents"]


    def __str__(self):
        return self.date

