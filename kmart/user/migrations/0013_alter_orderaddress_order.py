# Generated by Django 5.0 on 2024-02-15 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_orderaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddress',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='user.order'),
        ),
    ]
