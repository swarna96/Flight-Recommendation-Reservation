# Generated by Django 3.0.4 on 2020-11-19 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_input_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='Seat_no',
            new_name='Total_seat',
        ),
    ]
