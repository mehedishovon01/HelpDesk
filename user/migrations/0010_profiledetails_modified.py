# Generated by Django 4.2.7 on 2023-12-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_profiledetails_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]