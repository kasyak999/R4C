from django.urls import path
from .views import get_all_data, generate_robot_summary_excel


urlpatterns = [
    path('', get_all_data, name='get_all_data'),
    path('exel/', generate_robot_summary_excel, name='get_all_data'),
]
