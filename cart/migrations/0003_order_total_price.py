# Generated by Django 4.0.6 on 2024-02-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_order_address_remove_order_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='قیمت کل'),
        ),
    ]
