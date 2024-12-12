from django.urls import path
from . import views


urlpatterns = [
    path('waitlist/', views.add_to_waitlist, name='waitlist'),
]
