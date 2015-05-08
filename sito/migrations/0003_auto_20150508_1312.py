# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0002_auto_20150507_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categorie del Menu'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name_plural': 'Menu del Ristorante'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Pagine'},
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(null=True, verbose_name=b'Prezzo', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name=b'slider',
            field=image_cropping.fields.ImageRatioField(b'image', '1170x1170', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=b'Ritaglio Immagini per Slider', verbose_name=b'Slider'),
        ),
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Sottotitolo', blank=True),
        ),
    ]
