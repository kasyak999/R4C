from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_data, name='robots'),
    path('add/', views.add_production, name='add_production'),
    path('exel/', views.generate_robot_summary_excel, name='list_exel'),
]
