# Generated by Django 2.2.6 on 2020-01-06 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200106_2025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AvailableDays',
            new_name='AvailableDay',
        ),
    ]
