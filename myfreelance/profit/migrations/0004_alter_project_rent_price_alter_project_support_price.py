# Generated by Django 4.2.7 on 2023-12-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0003_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='rent_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость аренды сервера'),
        ),
        migrations.AlterField(
            model_name='project',
            name='support_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена поддержки'),
        ),
    ]
