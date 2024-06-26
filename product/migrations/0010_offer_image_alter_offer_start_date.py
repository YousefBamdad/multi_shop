# Generated by Django 4.0.6 on 2024-04-01 10:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_offer_options_offer_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='Image',
            field=models.ImageField(null=True, upload_to='', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 1, 10, 55, 1, 79814, tzinfo=utc), verbose_name='زمان شروع'),
        ),
    ]
