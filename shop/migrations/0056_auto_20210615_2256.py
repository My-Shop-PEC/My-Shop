# Generated by Django 3.1.7 on 2021-06-15 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0055_auto_20210615_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 22, 56, 1, 2705)),
        ),
    ]