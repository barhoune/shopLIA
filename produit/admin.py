from django.contrib import admin
from .models import Produit
# Register your models here.
class ProductAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview']
     list_display = ['name','img_preview']     
     search_fields=['name','description']
     list_filter=['categorie']
admin.site.register(Produit,ProductAdmin)