# Generated by Django 3.1.5 on 2021-01-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sytoapp', '0002_auto_20210128_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
