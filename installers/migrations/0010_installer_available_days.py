# Generated by Django 2.2.6 on 2020-02-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0009_auto_20200201_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='installer',
            name='available_days',
            field=models.TextField(null=True),
        ),
    ]