# Generated by Django 3.0.4 on 2020-11-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_auto_20201111_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Flight',
            field=models.CharField(max_length=50),
        ),
    ]