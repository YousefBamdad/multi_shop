# Generated by Django 4.0.6 on 2024-02-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_discountcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='عنوان و کد تخفیف'),
        ),
    ]
