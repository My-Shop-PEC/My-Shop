# Generated by Django 3.1.7 on 2021-06-12 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20210612_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 12, 19, 39, 28, 564090)),
        ),
    ]
