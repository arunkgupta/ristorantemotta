# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Titolo:')),
                ('description', models.TextField(null=True, verbose_name=b'Ingredienti del Piatto', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name=b'Titolo Piatto', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Ingredienti del Piatto', blank=True)),
                ('price', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Pubblicato')),
                ('categoria', models.ForeignKey(blank=True, to='sito.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Immagini',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, verbose_name=b'Titolo del Progetto:')),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('didascalia', models.TextField(null=True, blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                (b'slidepage', image_cropping.fields.ImageRatioField(b'image', '870x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='slidepage')),
                (b'croppingthumb', image_cropping.fields.ImageRatioField(b'image', '600x450', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingthumb')),
                (b'croppingslide', image_cropping.fields.ImageRatioField(b'image', '1140x487', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingslide')),
                (b'croppingcarousel', image_cropping.fields.ImageRatioField(b'image', '198x132', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingcarousel')),
                (b'croppingrender', image_cropping.fields.ImageRatioField(b'image', '1199x674', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingrender')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name_plural': 'Galleria Immagini',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name=b'Titolo', blank=True)),
                ('active', models.BooleanField(default=False, verbose_name=b'Pubblica?')),
                ('body', models.TextField(null=True, verbose_name=b'descrizione', blank=True)),
                ('image', models.ImageField(upload_to=b'uploaded_images', null=True, verbose_name=b'Immagine di Copertina', blank=True)),
                (b'thumb', image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=b'Ritaglio Immagini Miniatura', verbose_name=b'Miniatura')),
                (b'slider', image_cropping.fields.ImageRatioField(b'image', '1170x500', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=b'Ritaglio Immagini per Slider', verbose_name=b'Slider')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=b'Immagine Croppata', verbose_name=b'IMG Crop')),
                (b'freecropping', image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=b'Ritaglio Immagini Libero', verbose_name='freecropping')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name_plural': 'News - Eventi',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'Titolo:', blank=True)),
                ('body', models.TextField(null=True, verbose_name=b'Descrizione', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                (b'croppingminiatura', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Miniatura')),
                (b'croppingslider', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Slider')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Cropping')),
                (b'croppingfree', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name=b'Free Crop')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('galleria', models.ManyToManyField(to='sito.Immagini', null=True, verbose_name=b'Seleziona Immagini Galleria', blank=True)),
            ],
        ),
    ]
