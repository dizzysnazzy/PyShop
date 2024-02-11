from django.db import models
import os


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    # image_url = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.name



class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()