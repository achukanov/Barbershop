from django.db import models
from django.urls import reverse


class News(models.Model):
    content = models.TextField(max_length=350, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, editable=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Booking(models.Model):
    date = models.DateField(auto_now=False, verbose_name='Дата записи')
    time = models.TimeField(auto_now=False, verbose_name='Время записи')
    name = models.CharField(max_length=50, blank=True, verbose_name='Имя клиента')
    phone = models.IntegerField(verbose_name='Телефон')
    confirmed = models.BooleanField(default=False, verbose_name='Запись подтверждена')
    performed = models.BooleanField(default=False, verbose_name='Выполнено')
    сancel = models.BooleanField(default=False, verbose_name='Отменено')
    description = models.TextField(max_length=350, blank=True, verbose_name='Комментарии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заявки')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-date', '-time']
