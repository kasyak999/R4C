import json
from django.http import JsonResponse


def metod_post(request, form_class, message):
    form = form_class(json.loads(request.body))
    if form.is_valid():
        form.save()
        return JsonResponse(
            {'message': message}, status=201)
    else:
        return JsonResponse({'errors': form.errors}, status=400)
