# Generated by Django 4.2.7 on 2023-12-16 20:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profiledetails_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]