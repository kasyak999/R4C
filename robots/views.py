from datetime import timedelta
import json
import openpyxl
from openpyxl.styles import Font
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from .models import Robot
from .forms import RobotForm


@csrf_exempt
def get_all_data(request):
    """Вывести список роботов"""
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


def generate_robot_summary_excel(request):
    """Генерируем Exel файл для отчета за последную неделю"""
    week_start = timezone.now() - timedelta(days=7)
    wb = openpyxl.Workbook()
    sheet = wb.active
    wb.remove(sheet)
    robots = Robot.objects.prefetch_related('productionlog')
    models = robots.values_list('model', flat=True).distinct()

    for model in set(models):
        sheet = wb.create_sheet(title=f"{model}")
        sheet['A1'] = 'Модель'
        sheet['B1'] = 'Версия'
        sheet['C1'] = 'Количество за неделю'

        for cell in ['A1', 'B1', 'C1']:
            sheet[cell].font = Font(bold=True)

        robots_for_model = robots.filter(model=model)
        row = 2

        for robot in robots_for_model:
            production_logs = robot.productionlog.filter(
                production_date__gte=week_start
            )
            total_quantity = sum(log.quantity for log in production_logs)

            sheet[f'A{row}'] = robot.model
            sheet[f'B{row}'] = robot.version
            sheet[f'C{row}'] = total_quantity
            row += 1

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=robot.xlsx'
    wb.save(response)
    return response
