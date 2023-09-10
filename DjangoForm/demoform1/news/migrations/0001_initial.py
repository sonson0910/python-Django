# Generated by Django 2.2 on 2023-01-18 10:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('create_time', models.DateField(default=datetime.datetime(2023, 1, 18, 10, 17, 21, 212422, tzinfo=utc))),
            ],
        ),
    ]
