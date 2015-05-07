# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Titolo', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 5, 7, 14, 7, 56, 517242, tzinfo=utc), max_length=255, verbose_name=b'Titolo'),
            preserve_default=False,
        ),
    ]
