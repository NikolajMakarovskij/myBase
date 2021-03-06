# Generated by Django 4.0.5 on 2022-06-27 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_departament_post_remove_book_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Workplace',
        ),
        migrations.AddField(
            model_name='employee',
            name='departament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.departament'),
        ),
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.post'),
        ),
    ]
