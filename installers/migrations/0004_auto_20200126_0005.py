# Generated by Django 2.2.6 on 2020-01-26 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0003_auto_20200125_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
