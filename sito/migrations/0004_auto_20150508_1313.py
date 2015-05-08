# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0003_auto_20150508_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=b'Immagine Croppata', verbose_name=b'IMG Crop'),
        ),
        migrations.AlterField(
            model_name='news',
            name=b'slider',
            field=image_cropping.fields.ImageRatioField(b'image', '1170x1170', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=b'Ritaglio Immagini per Slider', verbose_name=b'Slider'),
        ),
        migrations.AlterField(
            model_name='news',
            name=b'thumb',
            field=image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=b'Ritaglio Immagini Miniatura', verbose_name=b'Miniatura'),
        ),
    ]
