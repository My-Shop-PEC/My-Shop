# Generated by Django 3.1.7 on 2021-06-15 05:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_auto_20210615_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 10, 47, 7, 103167)),
        ),
    ]