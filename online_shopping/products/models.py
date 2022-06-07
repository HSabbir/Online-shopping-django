from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from accounts.models import Customer
from .utils import slugify_instance_title

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class ProductQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
        return self.filter(lookups)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    number_of_ratings = models.IntegerField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # user_review need to be added
    discountRate = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)

    objects = ProductManager()

    @property
    def discount(self):
        if self.discountRate > 0:
            discounted_price = self.price - self.price * self.discountRate / 100
            return discounted_price
        return self.price

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=40)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='item',on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def get_total(self):
        total = self.product.discount * self.quantity
        return total

def slug_pre_save(sender,instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(slug_pre_save, sender=Product)
pre_save.connect(slug_pre_save, sender=ProductCategory)

def slug_post_save(sender,instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save= True)


post_save.connect(slug_post_save, sender=Product)
post_save.connect(slug_post_save, sender=ProductCategory)



