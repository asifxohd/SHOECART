# Generated by Django 4.2.6 on 2023-11-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('coupon_code', models.CharField(default=None, max_length=20, unique=True)),
                ('coupon_title', models.CharField(blank=True, max_length=250)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_type', models.CharField(blank=True, choices=[('flat', 'Flat'), ('percentage', 'Percentage')], default='percentage', max_length=10, null=True)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField(null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('minimum_order_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('maximum_order_amount_the_discount_percenetage_applicable_for', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('active', models.BooleanField(default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
