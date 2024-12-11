from django.shortcuts import render
from django.http import JsonResponse
from .models import Robot
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import RobotForm
from django.utils import timezone


@csrf_exempt
def get_all_data(request):
    if request.method == 'GET':
        result = list(Robot.objects.all().values(
            'model', 'version', 'created'))
        return JsonResponse(result, safe=False)
    elif request.method == 'POST':
        form = RobotForm(json.loads(request.body))
        if form.is_valid():
            robot = form.save(commit=False)
            robot.created = timezone.now().date()
            robot.serial = f'{robot.model}-{robot.version}'
            robot.save()
            return JsonResponse(
                {'message': 'Робот успешно добавлен'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Не поддерживается'}, status=404)
