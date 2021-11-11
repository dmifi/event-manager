from django.db import models


class EventUsersData(models.Model):
    """Данные о пользователях мероприятия"""
    date_time = models.DateTimeField("Дата и время", auto_now_add=True)
    weight_user = models.PositiveIntegerField("Масса")
    age_user = models.PositiveIntegerField("Возраст")
    text_a = models.CharField("Текст A", max_length=55)
    text_b = models.CharField("Текст B", max_length=55)
    description = models.CharField("Описание", max_length=250)
    status = models.BooleanField("Статус", default=False)

    def total_user(self):
        return self.weight_user - self.age_user

    def get_absolute_url(self):
        return "/"

    def __str__(self):
        return f'Данные №{self.pk}'

    class Meta:
        verbose_name = "Данные о пользователе мероприятия"
        verbose_name_plural = "Данные о пользователях мероприятия"
