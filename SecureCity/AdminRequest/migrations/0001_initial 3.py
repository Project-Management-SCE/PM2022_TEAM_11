# Generated by Django 4.0.4 on 2022-05-13 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRequest',
            fields=[
                ('userAsked', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('description', models.TextField(blank=True, max_length=150, null=True, verbose_name='description')),
            ],
        ),
    ]
