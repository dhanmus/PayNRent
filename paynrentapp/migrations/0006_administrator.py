# Generated by Django 4.1.6 on 2023-04-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0005_rename_fueltype_vehicle_fuel_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(default='', max_length=70)),
                ('mobileno', models.CharField(default='', max_length=15)),
                ('emailid', models.CharField(default='', max_length=150)),
                ('password', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
