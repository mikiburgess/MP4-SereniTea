"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Basket app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render, redirect


def view_basket(request):
    """ A view to return the shopping basket page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add specified quantity of selected item to the basket """
    
    # obtain submitted variable values
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    # add basket/content to session basket
    if item_id in list(basket.keys()):
        # item already in basket - increment quantity
        basket[item_id] += quantity
    else:
        # item not in basket - add quantity to basket
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
