from django.db import models
from django.urls import reverse
# Create your models here.
class Typesofpuja(models.Model):
    puja_img = models.ImageField( null=True) 
    title = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=10000, null=True)
    price = models.CharField(max_length=191, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): #this is to show the name in the admin panel, you will understand in the next tutorial
        return self.title 
    
    def get_absolute_url(self):
        return reverse("detailshome", args=[str(self.id)])
#even if you dont write this function, you will not face any issues 