# Generated by Django 5.0.1 on 2024-02-02 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0026_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateField(default=datetime.time(12, 34, 50, 461461)),
        ),
    ]