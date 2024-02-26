# Generated by Django 5.0.1 on 2024-02-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_orders_user_orders_booking_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(max_length=36, null=True, verbose_name='Payment ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='signature_id',
            field=models.CharField(max_length=128, null=True, verbose_name='Signature ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default='Pending', max_length=254, verbose_name='Payment Status'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_money',
            field=models.FloatField(null=True, verbose_name='Amount'),
        ),
    ]
