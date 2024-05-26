"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Home app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render
from django.conf import settings


def index(request):
    """ A view to return the site index (home) page """
    return render(request, 'home/index.html')


def about_serenitea(request):
    """ A view to return the About Serenitea page """
    return render(request, 'home/about_serenitea.html')


def shipping(request):
    """ A view to return the Shipping and Delivery information page """
    template = 'home/shipping.html'
    context = {
        'standard_delivery_charge': settings.STANDARD_DELIVERY_CHARGE,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }
    return render(request, template, context)
