"""
Product Admin for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.contrib import admin
from .models import Product, Category

# Register Models
admin.site.register(Product)
admin.site.register(Category)
