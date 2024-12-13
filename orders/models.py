from django.db import models
from customers.models import Customer


class PublishedModel(models.Model):
    """Базовая модель"""

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    robot_serial = models.CharField(
        max_length=5, blank=False, null=False, verbose_name='Робот')

    class Meta:
        abstract = True
        ordering = ('-id',)

    def __str__(self):
        return f'{self.customer} - {self.robot_serial}'


class Order(PublishedModel):

    class Meta(PublishedModel.Meta):
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
        default_related_name = 'orders'


class Waitlist(PublishedModel):

    class Meta(PublishedModel.Meta):
        verbose_name = 'ожидание'
        verbose_name_plural = 'Список ожидания'
        default_related_name = 'waitlist'
