from django.db import models

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
       return self.name
    