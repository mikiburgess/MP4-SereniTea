"""
Product Admin for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""
from django.contrib import admin
from .models import Product, Category


# Setup model admin classes
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'friendly_name',
        'name',
        'category',
        'price',
        'rating',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'friendly_name',
        'name',
        'group',
    )


# Register Models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
