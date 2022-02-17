# Generated by Django 4.0.2 on 2022-02-17 14:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(blank=True, max_length=5, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 2, 17, 14, 53, 30, 494103, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bodies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
