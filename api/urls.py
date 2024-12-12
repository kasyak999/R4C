from django.urls import path, include


urlpatterns = [
    path('', include('api.robots.urls')),
    path('', include('api.orders.urls')),
]
