from django.db import models
from django import forms
from image_cropping import ImageRatioField, ImageCropField

# Create your models here.
class Category(models.Model):
    title = models.CharField("Titolo:", max_length=100)
    description = models.TextField(blank=True, null=True, verbose_name="Ingredienti del Piatto")

    def __unicode__(self):
		return self.title
			
	class Meta:
		verbose_name_plural = "Galleria Immagini"
        ordering = ['-id']



class Immagini(models.Model):
	titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
	didascalia = models.TextField(null=True, blank=True)
	cropping = ImageRatioField('image', '500x480')
	slidepage = ImageRatioField('image', '870x480')
	croppingthumb = ImageRatioField('image', '600x450')
	croppingslide = ImageRatioField('image', '1140x487')
	croppingcarousel = ImageRatioField('image', '198x132')
	croppingrender = ImageRatioField('image', '1199x674')
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.titolo

	class Meta:
		verbose_name_plural = "Galleria Immagini"
        ordering = ['-id']



class Food(models.Model):
    categoria = models.ForeignKey(Category, null=True, blank=True)
    title = models.CharField(blank=True, null=True, max_length=255, verbose_name="Titolo Piatto")
    description = models.TextField(blank=True, null=True, verbose_name="Ingredienti del Piatto")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name="Pubblicato")
    def __unicode__(self):
    	return self.title
	class Meta:
		verbose_name_plural = "Menu del Ristorante"



class News(models.Model):
	title = models.CharField(blank=True, null=True, max_length=255, verbose_name="Titolo")
	active = models.BooleanField(default=False, verbose_name="Pubblica?")
	body = models.TextField(blank=True, null=True, verbose_name="descrizione")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images', verbose_name="Immagine di Copertina")
	thumb = ImageRatioField('image', '1200x1125', free_crop=True, verbose_name="Miniatura", help_text="Ritaglio Immagini Miniatura")
	slider = ImageRatioField('image', '1170x500', free_crop=True, verbose_name="Slider", help_text="Ritaglio Immagini per Slider")
	cropping = ImageRatioField('image', '1200x1125', free_crop=True, verbose_name="IMG Crop", help_text="Immagine Croppata")
	freecropping = ImageRatioField('image', '1200x1125', free_crop=True, help_text="Ritaglio Immagini Libero")
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.titolo

	class Meta:
		verbose_name_plural = "News - Eventi"



class Page(models.Model):
    title = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    croppingminiatura = ImageRatioField('image', '500x469', verbose_name="Miniatura")
    croppingslider = ImageRatioField('image', '500x469', verbose_name="Slider")
    cropping = ImageRatioField('image', '500x469', verbose_name="Cropping")
    croppingfree = ImageRatioField('image', '500x469', free_crop=True, verbose_name="Free Crop")
    galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

	class Meta:
		verbose_name_plural = "Pagine"






