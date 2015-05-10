from django.db import models
from django import forms
from image_cropping import ImageRatioField, ImageCropField


class Category(models.Model):
    title = models.CharField("Titolo:", max_length=100)
    description = models.TextField(blank=True, null=True, verbose_name="Ingredienti del Piatto")

    class Meta:
    	verbose_name_plural = "Categorie del Menu"

    def __unicode__(self):
		return self.title



class Immagini(models.Model):
	titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
	didascalia = models.TextField(null=True, blank=True)
	cropping = ImageRatioField('image', '500x480')
	slidepage = ImageRatioField('image', '870x480')
	croppingthumb = ImageRatioField('image', '600x450')
	croppingslide = ImageRatioField('image', '1170x500')
	croppingcarousel = ImageRatioField('image', '198x132')
	croppingrender = ImageRatioField('image', '1199x674')
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.titolo

	class Meta:
		verbose_name_plural = "Galleria Immagini"
        ordering = ['-id']



class Food(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255, verbose_name="Titolo Piatto")
    categoria = models.ForeignKey(Category, null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="Ingredienti del Piatto")
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name="Pubblicato")

    class Meta:
		verbose_name_plural = "Menu del Ristorante"
    
    def __unicode__(self):
    	#return self.title
    	return u'%s %s %s' % (self.title, self.price, self.categoria.title)



class News(models.Model):
	title = models.CharField(max_length=255, verbose_name="Titolo")
	subtitle = models.CharField(blank=True, null=True, max_length=255, verbose_name="Sottotitolo")
	active = models.BooleanField(default=False, verbose_name="Pubblica?")
	body = models.TextField(blank=True, null=True, verbose_name="descrizione")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images', verbose_name="Immagine di Copertina")
	thumb = ImageRatioField('image', '1200x1125', verbose_name="Miniatura", help_text="Ritaglio Immagini Miniatura")
	slider = ImageRatioField('image', '1170x500', verbose_name="Slider", help_text="Ritaglio Immagini per Slider")
	cropping = ImageRatioField('image', '1200x1125', verbose_name="IMG Crop", help_text="Immagine Croppata")
	freecropping = ImageRatioField('image', '1200x1125', free_crop=True, help_text="Ritaglio Immagini Libero")
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name_plural = "News - Eventi"



class Page(models.Model):
    title = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    croppingminiatura = ImageRatioField('image', '500x500', verbose_name="Miniatura")
    croppingslider = ImageRatioField('image', '1170x500', verbose_name="Slider")
    cropping = ImageRatioField('image', '500x469', verbose_name="Cropping")
    croppingfree = ImageRatioField('image', '500x469', free_crop=True, verbose_name="Free Crop")
    #galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    pub_date = models.DateTimeField('date published')

    class Meta:
    	verbose_name_plural = "Pagine"

    def __unicode__(self):
        return self.title



class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cognome = forms.CharField(label='Cognome', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=100, required = False)
    fax = forms.CharField(label='Fax', max_length=100, required = False)
    email = forms.CharField(label='email', max_length=100)
    citta = forms.CharField(label='Citta', max_length=100, required = False)
    indirizzo = forms.CharField(label='Indirizzo', max_length=100, required = False)
    messaggio = forms.CharField(label='Messaggio', widget=forms.Textarea, required = False)