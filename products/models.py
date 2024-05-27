"""
Product Models for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    friendly_name = models.CharField(max_length=200, null=False,
                                     default="Product Category")
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=10, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=False,
                                     default="Store Product")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    alt_text = models.TextField(null=True, blank=True)
    bs_icon = models.CharField(max_length=100, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    organic = models.CharField(max_length=3, null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    brew_time = models.CharField(max_length=10, null=True, blank=True)
    water_temp = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, null=False, decimal_places=2)
    stock_level = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, 
                                 blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_summary(self):
        return (f'{self.friendly_name} [sku: {self.sku[0:6]}] @ £{self.price}')
