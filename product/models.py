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
    


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"Order by {self.name} - {self.email}"