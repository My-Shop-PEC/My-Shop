# Generated by Django 3.1.7 on 2021-06-16 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0062_auto_20210616_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 16, 6, 34, 46, 910235)),
        ),
    ]