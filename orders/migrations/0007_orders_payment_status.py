# Generated by Django 4.2.6 on 2023-11-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_ordersitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.CharField(default='Pending', max_length=255),
        ),
    ]
