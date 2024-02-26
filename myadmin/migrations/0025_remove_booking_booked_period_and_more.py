# Generated by Django 5.0.1 on 2024-02-02 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0024_alter_booking_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booked_period',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.date(2024, 2, 2)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateField(default=datetime.time(18, 1, 32, 355497)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='token_money',
            field=models.FloatField(null=True),
        ),
    ]