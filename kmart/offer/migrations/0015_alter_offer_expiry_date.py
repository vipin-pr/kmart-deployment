# Generated by Django 5.0 on 2024-03-01 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0014_alter_offer_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 31, 19, 20, 1, 46262)),
        ),
    ]
