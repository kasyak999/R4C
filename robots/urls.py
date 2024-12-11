from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_data, name='robots'),
    path('exel/', views.generate_robot_summary_excel, name='list_exel'),
]
