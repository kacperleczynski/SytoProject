# Generated by Django 3.1.5 on 2021-01-29 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sytoapp', '0006_auto_20210129_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
    ]