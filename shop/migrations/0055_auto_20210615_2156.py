# Generated by Django 3.1.7 on 2021-06-15 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0054_auto_20210615_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 21, 56, 58, 283785)),
        ),
    ]
