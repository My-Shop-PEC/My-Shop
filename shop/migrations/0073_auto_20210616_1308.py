# Generated by Django 3.1.7 on 2021-06-16 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0072_auto_20210616_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 16, 13, 8, 36, 687940)),
        ),
    ]
