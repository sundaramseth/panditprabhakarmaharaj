from django.db import models
# Create your models here.
class BookingForm(models.Model):
    your_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    category= models.CharField(max_length=200)
    pujaname = models.CharField(max_length=200)
    puja_date=models.DateField()
    user_address=models.TextField()


    def __str__(self):
        return self.your_name
    

class SubscribeForm(models.Model):
    subscriber = models.EmailField(max_length=200)

    def __str__(self):
        return self.subscriber