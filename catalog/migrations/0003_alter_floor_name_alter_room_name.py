# Generated by Django 4.0.5 on 2022-06-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_building_floor_room_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='name',
            field=models.CharField(help_text='Введите номер этажа', max_length=15),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(help_text='Введите номер кабинета', max_length=15),
        ),
    ]