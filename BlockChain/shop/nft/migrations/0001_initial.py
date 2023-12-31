# Generated by Django 3.2.17 on 2023-02-11 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('Type', models.CharField(default='', max_length=10)),
                ('metadata', models.CharField(default='', max_length=100)),
                ('policy_id', models.CharField(default='', max_length=100)),
                ('data', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
