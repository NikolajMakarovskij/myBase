# Generated by Django 4.0.5 on 2022-06-26 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_employee_building_alter_employee_floor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите номер пользователя', max_length=50)),
                ('Building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.building')),
                ('Floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.floor')),
                ('Room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.room')),
            ],
            options={
                'verbose_name_plural': 'Рабочее место',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='Workplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace'),
        ),
    ]
