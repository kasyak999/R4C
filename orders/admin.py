from django.contrib import admin
from .models import Order, Waitlist


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer', 'robot_serial')
    list_display_links = ('customer',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Waitlist, OrderAdmin)
