# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(default=datetime.date.today)),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]
