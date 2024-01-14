from django.db import models

# Create your models here.
class BookingForm(models.Model):
    your_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    category= models.CharField(max_length=20)
    puja_date=models.DateField();
    puja_item=models.BooleanField()
    user_adress=models.TextField();
    details=models.TextField();


    def __str__(self):
        return self.your_name