from django.urls import path
from . import views


urlpatterns = [
    path('waitlist/', views.add_order, name='waitlist'),
]
