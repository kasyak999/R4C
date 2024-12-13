from django.urls import path
from . import views


urlpatterns = [
    path('order/', views.add_order, name='order'),
]
