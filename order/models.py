from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from produit.models import Produit

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    qte = models.IntegerField(default=1)
    dateOrder = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, related_name='orders', on_delete=models.CASCADE)

    def total(self):
        qte=int(self.qte)
        price=int(self.product.price)
        total=qte*price
        return total
    
    def __str__(self):
        qte=int(self.qte)
        price=int(self.product.price)
        total=qte*price
        return "name: "+ self.user.username +" Product: "+ self.product.name +" Quantity: "+ str(self.qte)+" Price: "+str(self.product.price) +" Totale: "+ str(total)
