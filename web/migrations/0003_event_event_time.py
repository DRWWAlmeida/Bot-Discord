# Generated by Django 5.0 on 2024-01-04 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_event_author_event_created_at_event_is_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2024, 1, 4, 23, 0, 48, 509188, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
