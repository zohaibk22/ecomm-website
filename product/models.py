from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    discounted_price = models.FloatField()

    def __str__(self):
        return f"{self.name}"