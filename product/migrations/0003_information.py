# Generated by Django 4.0.6 on 2024-01-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_color_options_alter_size_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن')),
            ],
            options={
                'verbose_name': 'اطلاعات تکمیلی',
                'verbose_name_plural': 'اطلاعات تکمیلی',
            },
        ),
    ]
