
# Generated by Django 4.0.3 on 2022-05-24 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Patrols', '0004_alter_patrol_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrol',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2022, 5, 24, 21, 8, 20, 760770, tzinfo=utc), verbose_name='end time'),
        ),
    ]
