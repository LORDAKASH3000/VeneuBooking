# Generated by Django 5.0.1 on 2024-01-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='venue_img'),
        ),
    ]
