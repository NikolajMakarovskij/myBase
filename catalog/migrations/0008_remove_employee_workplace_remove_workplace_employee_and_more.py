# Generated by Django 4.0.5 on 2022-06-26 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_rename_floor_room_employee_remove_employee_building_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Workplace',
        ),
        migrations.RemoveField(
            model_name='workplace',
            name='Employee',
        ),
        migrations.AlterField(
            model_name='room',
            name='Employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.employee'),
        ),
    ]
