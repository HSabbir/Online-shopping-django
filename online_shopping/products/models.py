from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    number_of_ratings = models.IntegerField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # user_review need to be added
    available_stock = models.IntegerField(default=0)
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

