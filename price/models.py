from django.db import models

class PriceList(models.Model):
    title = models.CharField(max_length=30, verbose_name='Услуга')
    price = models.IntegerField(verbose_name='Цена')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

