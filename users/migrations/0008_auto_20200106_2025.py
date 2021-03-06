# Generated by Django 2.2.6 on 2020-01-06 20:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_availabledays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabledays',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=56),
        ),
    ]
