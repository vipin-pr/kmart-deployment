# Generated by Django 5.0 on 2024-02-16 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_unique_admin', '0008_alter_coupon_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 18, 0, 30, 14, 938922)),
        ),
    ]
