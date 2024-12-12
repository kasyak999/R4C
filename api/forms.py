from django import forms
from robots.models import Robot, ProductionLog
from orders.models import Order


class RobotForm(forms.ModelForm):

    class Meta:
        model = Robot
        fields = ['model', 'version']


class ProductionForm(forms.ModelForm):

    class Meta:
        model = ProductionLog
        fields = ['robot', 'quantity']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['customer', 'robot_serial']
