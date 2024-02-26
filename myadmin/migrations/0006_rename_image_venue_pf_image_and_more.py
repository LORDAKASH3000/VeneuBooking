# Generated by Django 5.0.1 on 2024-01-30 15:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_alter_booking_booking_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='image',
            new_name='pf_image',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(verbose_name=datetime.date(2024, 1, 30)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(verbose_name=datetime.time(21, 12, 35, 618038)),
        ),
        migrations.CreateModel(
            name='VenueImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.ImageField(upload_to='venue_img')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myadmin.venue')),
            ],
        ),
    ]
