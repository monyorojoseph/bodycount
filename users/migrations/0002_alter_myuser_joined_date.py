# Generated by Django 4.0.2 on 2022-02-18 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 18, 10, 12, 7, 815517, tzinfo=utc)),
        ),
    ]
