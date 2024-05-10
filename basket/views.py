"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Basket app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render


def view_basket(request):
    """ A view to return the shopping basket page """
    return render(request, 'basket/basket.html')
