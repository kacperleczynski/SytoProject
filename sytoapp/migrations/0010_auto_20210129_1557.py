# Generated by Django 3.1.5 on 2021-01-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sytoapp', '0009_auto_20210129_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]