# Generated by Django 5.0 on 2024-02-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_order_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
