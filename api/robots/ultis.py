from django.core.mail import send_mail
from orders.models import Waitlist


def notify_customers(value):
    orders = Waitlist.objects.filter(robot_serial=value)
    recipient_list = [order.customer.email for order in orders]
    send_mail(
        subject='Робот есть в наличии',
        message=(
            'Добрый день!\n'
            'Недавно вы интересовались нашим роботом модели '
            f'{value.robot.model}, версии {value.robot.version}.\n'
            'Этот робот теперь в наличии. Если вам подходит '
            'этот вариант - пожалуйста, свяжитесь с нами.'
        ),
        from_email='from@example.com',
        recipient_list=recipient_list,
        fail_silently=True,
    )
    orders.delete()
