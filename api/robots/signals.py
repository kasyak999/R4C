from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from robots.models import ProductionLog
from orders.models import Waitlist


@receiver(post_save, sender=ProductionLog)
def notify_customers(sender, instance, created, **kwargs):
    """Отправка письма клиенту"""
    if created:
        orders = Waitlist.objects.filter(
            robot_serial=instance).select_related('customer')
        recipient_list = set(order.customer.email for order in orders)
        send_mail(
            subject='Робот есть в наличии',
            message=(
                'Добрый день!\n'
                'Недавно вы интересовались нашим роботом модели '
                f'{instance.robot.model}, версии {instance.robot.version}.\n'
                'Этот робот теперь в наличии. Если вам подходит '
                'этот вариант - пожалуйста, свяжитесь с нами.'
            ),
            from_email='from@example.com',
            recipient_list=recipient_list,
            fail_silently=True,
        )
        orders.delete()
