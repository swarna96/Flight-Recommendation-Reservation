# Generated by Django 3.0.4 on 2020-11-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_auto_20201119_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Available',
            field=models.IntegerField(default=models.IntegerField()),
        ),
    ]
