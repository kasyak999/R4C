from django.contrib import admin
from .models import Robot, ProductionLog
# Register your models here.

admin.site.register(Robot, admin.ModelAdmin)
admin.site.register(ProductionLog, admin.ModelAdmin)
