# Generated by Django 4.0.4 on 2022-05-01 14:04

import django.contrib.postgres.fields
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('device_id', models.CharField(max_length=100)),
                ('manual_mode', models.BooleanField(default=False)),
                ('moisture_level', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=main.models.get_default_array, size=None)),
                ('temperature', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=main.models.get_default_array, size=None)),
                ('humidity', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=main.models.get_default_array, size=None)),
            ],
        ),
    ]