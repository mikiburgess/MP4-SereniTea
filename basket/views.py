"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Basket app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render, redirect, reverse, HttpResponse


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
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Update product quantities in shopping basket basket """

    # obtain submitted variable values
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    # update item quantity in basket
    if quantity > 0:
        # update item quantity
        basket[item_id] = quantity
    else:
        # remove item from basket
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket """

    try:
        # If item is in the basket, remove it and update basket contents
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)
    
    # If item not in basket, exception is raised and deletion not possible
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
