# Generated by Django 5.0.1 on 2024-01-30 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_remove_venue_gallery_venueimage_venue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(verbose_name=datetime.time(22, 19, 34, 385450)),
        ),
    ]
