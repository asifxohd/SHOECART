# Generated by Django 4.2.7 on 2023-11-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orders_total_purchase_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersitem',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
