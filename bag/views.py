"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Bag app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render


def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'bag/bag.html')
