# Generated by Django 3.1.7 on 2021-06-15 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_auto_20210615_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 18, 47, 10, 870280)),
        ),
    ]
