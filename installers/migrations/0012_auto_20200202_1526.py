# Generated by Django 2.2.6 on 2020-02-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0011_auto_20200202_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='installer',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='installer',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='installer',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='installer',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='installer',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='installer',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]
