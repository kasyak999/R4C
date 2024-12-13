import json
from django.db.models import Sum
from robots.models import Robot
from orders.models import Order
from api.forms import OrderForm, WaitlistForm


def handle_robot_order(request):
    data = json.loads(request.body)
    robot_serial = data.get('robot_serial')
    robot = Robot.objects.filter(serial=robot_serial).first()

    if not robot:
        return {'error': 'Такого робота не существует'}, 400

    produced_quantity = robot.productionlog.aggregate(
        Sum('quantity'))['quantity__sum'] or 0
    orders_count = Order.objects.filter(robot_serial=robot_serial).count()
    available_quantity = produced_quantity - orders_count

    if available_quantity < 1:
        form = WaitlistForm(data)
        message = 'Вы добавлены в список ожидания'
    else:
        form = OrderForm(data)
        message = 'Вы успешно добавили заказ'

    if form.is_valid():
        form.save()
        return {'message': message}, 201

    return {'errors': form.errors}, 400
