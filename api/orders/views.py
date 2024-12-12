import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.forms import OrderForm
from customers.models import Customer


@csrf_exempt
def add_to_waitlist(request):
    if request.method == 'POST':
        # form = OrderForm(json.loads(request.body))
        data = json.loads(request.body)
        email = data.get('customer')
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return JsonResponse({'error': f"Пользователь с email '{email}' не найден."}, status=404)

        data['customer'] = customer.id
        form = OrderForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Вы добавлены в список ожидания'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Не поддерживается'}, status=404)
