# Generated by Django 5.0 on 2024-02-15 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_unique_admin', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 16, 19, 27, 35, 4709)),
        ),
    ]