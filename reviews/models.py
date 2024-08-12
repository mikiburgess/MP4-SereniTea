"""
Product Review Model for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""
import uuid  # for generating unique review numbers

from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    RATING = [
        (0, "None"),
        (1, "Poor"),
        (2, "Ok"),
        (3, "Average"),
        (4, "Good"),
        (5, "Excellent"),
    ]

    review_code = models.CharField(max_length=32, null=False, editable=False)    
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    stars = models.IntegerField(choices=RATING, default='0')
    comment = models.TextField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


    def _generate_review_code(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()


    def __str__(self):
        """ Return review code and product SKU """
        return f'REVIEW {self.review_code} for SKU {self.product.sku}'
    

    def save(self, *args, **kwargs):
        """ Add the creation of a unique review id number to the save method
        """
        if not self.review_code:
            self.review_code = self._generate_review_code()
        super().save(*args, **kwargs)
