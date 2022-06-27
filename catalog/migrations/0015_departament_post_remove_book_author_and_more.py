# Generated by Django 4.0.5 on 2022-06-27 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_workplace_employee_workplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название отдела', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Отдел',
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите должность', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Должность',
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(help_text='Введите ФИО сотрудника', max_length=50),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='name',
            field=models.CharField(help_text='Введите номер рабочего места', max_length=50),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='post',
            name='Employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.employee'),
        ),
        migrations.AddField(
            model_name='post',
            name='Workplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace'),
        ),
        migrations.AddField(
            model_name='post',
            name='departament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.departament'),
        ),
    ]
