# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='bar',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 2, 3, 52, 608927, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bar',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 13, 2, 4, 5, 281905, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='bar',
            field=models.ForeignKey(to='main.Bar', related_name='reviews_bar'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reviews_user'),
        ),
    ]
