# Generated by Django 4.2.7 on 2023-12-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0005_project_server_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_server_mine',
            field=models.BooleanField(blank=True, null=True, verbose_name='На моём сервере'),
        ),
        migrations.AlterField(
            model_name='project',
            name='rent_next_payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата следующей оплаты сервера'),
        ),
        migrations.AlterField(
            model_name='project',
            name='support',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Поддержка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='support_next_payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата следующей оплаты поддержки'),
        ),
    ]