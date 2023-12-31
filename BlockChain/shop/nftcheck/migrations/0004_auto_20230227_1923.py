# Generated by Django 3.2.17 on 2023-02-27 12:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nftcheck', '0003_alter_checker_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checker',
            name='assetID',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='checker',
            name='policyID',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='checker',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 12, 23, 55, 193031, tzinfo=utc)),
        ),
    ]
