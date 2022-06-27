# Generated by Django 4.0.5 on 2022-06-24 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(help_text='Введите номер этажа')),
                ('Building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.building')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(help_text='Введите номер кабинета')),
                ('Building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.building')),
                ('Floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.floor')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите номер пользователя', max_length=50)),
                ('Building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.building')),
                ('Floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.floor')),
                ('Room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.room')),
            ],
        ),
    ]