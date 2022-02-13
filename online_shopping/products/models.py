from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    number_of_ratings = models.IntegerField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # user_review need to be added
    discount_rate = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def discount(self):
        if self.discount_rate > 0:
            discounted_price = self.price - self.price * self.discount_rate / 100
            return discounted_price
        return self.price



