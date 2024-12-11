from django.db import models
from django.utils import timezone


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    class Meta:
        """Перевод модели"""
        verbose_name = 'робот'
        verbose_name_plural = 'Роботы'
        constraints = [
            models.UniqueConstraint(
                fields=['model', 'version'],
                name='unique_model_version'
            )
        ]
        ordering = ('serial',)
        default_related_name = 'robots'

    def __str__(self):
        return f'{self.serial}'


class ProductionLog(models.Model):
    robot = models.ForeignKey(
        Robot, on_delete=models.CASCADE, verbose_name='Робот')
    production_date = models.DateField(
        default=timezone.now, verbose_name='Дата')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        """Перевод модели"""
        verbose_name = 'производство'
        verbose_name_plural = 'Журнал производства'
        ordering = ('robot',)
        default_related_name = 'productionlog'

    def __str__(self):
        return f'{self.robot}'
