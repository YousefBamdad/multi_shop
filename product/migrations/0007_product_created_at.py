# Generated by Django 4.0.6 on 2024-02-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_category_options_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]