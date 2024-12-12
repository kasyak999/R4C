from django.contrib import admin
from .models import Order, Waitlist


admin.site.register(Order, admin.ModelAdmin)
admin.site.register(Waitlist, admin.ModelAdmin)
