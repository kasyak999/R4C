from django.db import models


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

    def __str__(self):
        return f'{self.serial}'
