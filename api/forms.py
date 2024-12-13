from django import forms
from robots.models import Robot, ProductionLog
from orders.models import Order, Waitlist
from django.utils import timezone


class RobotForm(forms.ModelForm):

    class Meta:
        model = Robot
        fields = ['model', 'version']

    def save(self, commit=True):
        robot = super().save(commit=False)
        robot.created = timezone.now().date()
        robot.serial = f'{robot.model}-{robot.version}'
        if commit:
            robot.save()
        return robot


class ProductionForm(forms.ModelForm):

    class Meta:
        model = ProductionLog
        fields = ['robot', 'quantity']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['customer', 'robot_serial']


class WaitlistForm(forms.ModelForm):

    class Meta:
        model = Waitlist
        fields = ['customer', 'robot_serial']
