# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('yelp_id', models.CharField(max_length=300)),
                ('review_count', models.IntegerField(default=0)),
                ('happy_times', models.CharField(max_length=300, blank=True)),
            ],
        ),
    ]
