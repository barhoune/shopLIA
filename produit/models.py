from django.db import models
from category.models import Category
from django.utils.html import mark_safe
# Create your models here.
class Produit(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000,default="")
    price=models.IntegerField(default=1)
    date=models.DateTimeField(null=True)
    quantity=models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',null=True)
    categorie = models.ForeignKey(Category,related_name='cproducts',default=1, on_delete=models.CASCADE)
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" height = "150"/>')
    def __str__(self):
       return self.name
   