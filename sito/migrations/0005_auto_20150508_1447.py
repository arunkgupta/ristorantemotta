# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0004_auto_20150508_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name=b'slider',
            field=image_cropping.fields.ImageRatioField(b'image', '1170x500', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=b'Ritaglio Immagini per Slider', verbose_name=b'Slider'),
        ),
    ]
