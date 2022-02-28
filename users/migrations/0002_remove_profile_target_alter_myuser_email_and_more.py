# Generated by Django 4.0.2 on 2022-02-28 21:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='target',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 21, 59, 20, 926482, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=django_cryptography.fields.encrypt(models.CharField(default='18', max_length=10)),
        ),
    ]
