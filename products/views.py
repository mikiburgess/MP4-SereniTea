"""
Product Views for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""
from django.shortcuts import render, get_object_or_404
from .models import Product


# Product app views

def all_products(request):
    """ View to show all products """
    products = Product.objects.all()
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to show details of individual products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
