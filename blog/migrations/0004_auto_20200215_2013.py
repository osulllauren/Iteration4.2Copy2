# Generated by Django 2.2.6 on 2020-02-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200215_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='monday',
            field=models.BooleanField(default=False),
        ),
    ]
