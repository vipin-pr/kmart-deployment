# Generated by Django 5.0 on 2024-02-29 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0008_alter_offer_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 30, 10, 23, 5, 980858)),
        ),
    ]
