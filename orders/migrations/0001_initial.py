# Generated by Django 5.1.4 on 2024-12-13 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot_serial', models.CharField(max_length=5, verbose_name='Робот')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('id',),
                'abstract': False,
                'default_related_name': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot_serial', models.CharField(max_length=5, verbose_name='Робот')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'ожидание',
                'verbose_name_plural': 'Список ожидания',
                'ordering': ('id',),
                'abstract': False,
                'default_related_name': 'waitlist',
            },
        ),
    ]
