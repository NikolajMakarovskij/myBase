# Generated by Django 4.0.6 on 2022-07-20 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_alter_software_options_remove_workstation_software_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['name', 'Workplace'], 'verbose_name_plural': 'Сотрудник'},
        ),
        migrations.AlterModelOptions(
            name='software',
            options={'ordering': ['Employee', 'name'], 'verbose_name_plural': 'ПО'},
        ),
    ]
