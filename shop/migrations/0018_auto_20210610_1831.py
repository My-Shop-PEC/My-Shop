# Generated by Django 3.1.7 on 2021-06-10 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20210610_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 18, 31, 4, 879933)),
        ),
    ]