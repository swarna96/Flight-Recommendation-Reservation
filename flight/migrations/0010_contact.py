# Generated by Django 3.0.4 on 2020-11-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0009_auto_20201119_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('subject', models.TextField()),
            ],
        ),
    ]