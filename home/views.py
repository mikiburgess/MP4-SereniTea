"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Home app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render


def index(request):
    """ A view to return the site index (home) page """
    return render(request, 'home/index.html')


def about_serenitea(request):
    """ A view to return the About Serenitea page """
    return render(request, 'home/about_serenitea.html')
