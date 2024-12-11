from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_data, name='get_all_data'),
    path('exel/', views.generate_robot_summary_excel, name='get_all_data'),
]
