from django.db import models
class Product(models.Model):
    title       = models.CharField(max_length=120)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(null = False, blank = False)
    featured    = models.BooleanField(default= True)
    picture     = models.TextField(default= "https://www.schild.de/wp-content/uploads/2016/08/nopic.jpg")
    cart        = models.BooleanField(default= False)

    

# Create your models here.
