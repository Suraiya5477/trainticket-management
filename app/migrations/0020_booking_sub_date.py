# Generated by Django 4.0.2 on 2022-03-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_booking_travel_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='sub_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
