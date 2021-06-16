from django.db import models
from ecommerce_shop.models import Product


class Customer(models.Model):
    first_name = models.CharField(verbose_name='Имя клиента', max_length=250)
    last_name = models.CharField(verbose_name='Фамилия клиента', max_length=250)
    email = models.EmailField(verbose_name='Email клиента', max_length=250)
    phone = models.CharField(verbose_name='Номер телефона клиента', max_length=250)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Заказаный товар", null=True)
    date_created = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
