"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Basket app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ A view to return the shopping basket page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add specified quantity of selected item to the basket """

    # retrieve full product details
    product = Product.objects.get(pk=item_id)

    # obtain submitted variable values
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    # add basket/content to session basket
    if item_id in list(basket.keys()):
        # item already in basket - increment quantity
        basket[item_id] += quantity
        # inform customer that product quantity successfully updated
        messages.success(request, f'Updated {product.friendly_name} quantity in {basket[item_id]}')
    else:
        # item not in basket - add quantity to basket
        basket[item_id] = quantity
        # inform customer that product successfully added
        messages.success(request, f'Added {product.friendly_name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Update product quantities in shopping basket basket """

    # retrieve full product details
    product = Product.objects.get(pk=item_id)

    # obtain submitted variable values
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    # update item quantity in basket
    if quantity > 0:
        # update item quantity
        basket[item_id] = quantity
        # inform customer that product quantity successfully updated
        messages.success(request, f'Quantity of {product.friendly_name} updated in your basket to {quantity}')
    else:
        # remove item from basket
        basket.pop(item_id)
        # inform customer that product successfully removed
        messages.success(request, f'Removed {product.friendly_name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket """

    # retrieve full product details
    product = Product.objects.get(pk=item_id)

    try:
        # If item is in the basket, remove it and update basket contents
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket

        # inform customer that product successfully removed
        messages.success(request, f'Removed {product.friendly_name} from your basket')
        return HttpResponse(status=200)

    # If item not in basket, exception is raised and deletion not possible
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
