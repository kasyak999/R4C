from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import handle_robot_order


@csrf_exempt
def add_order(request):
    """Добавить заказ на робота"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Не поддерживается'}, status=404)
    response_data, status_code = handle_robot_order(request)
    return JsonResponse(response_data, status=status_code)
