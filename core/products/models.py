from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('products:category_products', kwargs={'pk': self.pk})


class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, related_name='products')
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    in_stock = models.BooleanField()

    def get_absolute_url(self):
        return reverse('products:product', kwargs={'pk': self.pk})


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_img', blank=True)
