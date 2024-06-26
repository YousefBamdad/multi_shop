# Generated by Django 4.0.6 on 2024-01-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='نام')),
                ('description', models.TextField(verbose_name='توضیحات محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('discount', models.SmallIntegerField(blank=True, null=True, verbose_name='تخفیف')),
                ('image', models.ImageField(upload_to='products', verbose_name='تصویر')),
                ('color', models.ManyToManyField(related_name='products', to='product.color', verbose_name='رنگ')),
                ('size', models.ManyToManyField(related_name='products', to='product.size', verbose_name='سایز')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
