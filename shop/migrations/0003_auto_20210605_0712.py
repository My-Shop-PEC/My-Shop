# Generated by Django 3.1.7 on 2021-06-05 01:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210605_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='delivery_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='ordered_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 7, 12, 32, 207696)),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='ending_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
