# Generated by Django 4.0.6 on 2024-01-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_otp_alter_user_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otp',
            options={'verbose_name': 'اعتبارسنجی', 'verbose_name_plural': 'اعتبارسنجی ها'},
        ),
        migrations.AddField(
            model_name='otp',
            name='token',
            field=models.CharField(max_length=50, null=True),
        ),
    ]