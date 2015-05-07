from django.contrib import admin
from sito.models import *

from image_cropping import ImageCroppingMixin

# Register your models here.
'''
def get_categoria(self):
    return self.categoria.title
'''

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class FoodAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("title", "price", "categoria")

admin.site.register(Category, MyModelAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(News, MyModelAdmin)
admin.site.register(Immagini, MyModelAdmin)
admin.site.register(Page, MyModelAdmin)
