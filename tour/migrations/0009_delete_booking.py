# Generated by Django 5.1.4 on 2024-12-15 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_remove_booking_booking_date_booking_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
