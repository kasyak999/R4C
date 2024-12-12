import json
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from api.forms import OrderForm, WaitlistForm
from robots.models import Robot
from orders.models import Order


@csrf_exempt
def add_order(request):
    """Добавить заказ на робота"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Не поддерживается'}, status=404)

    data = json.loads(request.body)
    robots = Robot.objects.filter(serial=data['robot_serial']).first()
    if not robots:
        return JsonResponse(
            {'errors': 'Такого робота не существует'}, status=400)

    produced = robots.productionlog.aggregate(
        Sum('quantity'))['quantity__sum']
    orders = Order.objects.filter(
        robot_serial=data['robot_serial']).count()
    available_quantity = produced - orders

    if available_quantity < 1:
        form_class = WaitlistForm
        message = 'Вы добавлены в список ожидания'
    else:
        form_class = OrderForm
        message = 'Вы успешно добавили заказ'

    form = form_class(data)
    if form.is_valid():
        form.save()
        return JsonResponse(
            {'message': message}, status=201)
    else:
        return JsonResponse({'errors': form.errors}, status=400)
