# Generated by Django 4.0.5 on 2022-07-13 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_remove_post_employee_remove_post_workplace_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите Название ОС', max_length=50)),
                ('licenseKeyText', models.CharField(blank=True, help_text='Введите лицензтонный ключ', max_length=50, null=True)),
                ('licenseKeyImg', models.ImageField(blank=True, height_field='20px', help_text='прикрепите файл', max_length=50, null=True, upload_to='', width_field='100px')),
            ],
            options={
                'verbose_name_plural': 'ОС',
            },
        ),
        migrations.CreateModel(
            name='software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ВВедите название ПО', max_length=50)),
                ('licenseKeyText', models.CharField(blank=True, help_text='Введите лицензтонный ключ', max_length=50, null=True)),
                ('licenseKeyImg', models.ImageField(blank=True, height_field='20px', help_text='прикрепите файл', max_length=50, null=True, upload_to='', width_field='100px')),
            ],
            options={
                'verbose_name_plural': 'Рабочая станция',
            },
        ),
        migrations.CreateModel(
            name='workstation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите номер станции', max_length=50)),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.employee')),
                ('OS', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.os')),
                ('Workplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace')),
                ('software', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.software')),
            ],
            options={
                'verbose_name_plural': 'Рабочая станция',
            },
        ),
    ]
