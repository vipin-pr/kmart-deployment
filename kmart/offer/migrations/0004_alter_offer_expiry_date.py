# Generated by Django 5.0 on 2024-02-21 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_alter_offer_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 14, 55, 25, 560263)),
        ),
    ]