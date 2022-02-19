# Generated by Django 4.0.2 on 2022-02-18 10:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('body', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_title', models.CharField(max_length=200)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Votes',
            },
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-id'], 'verbose_name': 'Person'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id'], 'verbose_name': 'Review'},
        ),
        migrations.RenameField(
            model_name='review',
            old_name='comments',
            new_name='review_text',
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 18, 10, 12, 7, 811515, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repy_text', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reply',
                'ordering': ['-id'],
            },
        ),
    ]