from django.contrib import admin
from .models import Robot, ProductionLog


class RobotAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'serial', 'created')
    list_display_links = ('serial',)


class ProductionLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'robot', 'quantity', 'production_date')
    list_display_links = ('robot',)


admin.site.register(Robot, RobotAdmin)
admin.site.register(ProductionLog, ProductionLogAdmin)
