"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Context Processor for the Basket App
- - - - - - - - - - - - - - - - - - - -
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """ Context processor for basket contents """

    # Initialise shopping basket and initial costs
    basket_items = []
    items_count = 0
    items_total = 0
    grand_total = 0.0
    standard_delivery = Decimal(settings.STANDARD_DELIVERY_CHARGE)
    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)

    # Get current basket contents from session variable
    basket = request.session.get('basket', {})

    # Update contents of basket
    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        items_total += quantity * product.price
        items_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Calculate current costs and delivery charge
    if 0 < items_total < free_delivery_threshold:
        delivery = standard_delivery
        amount_to_spend = free_delivery_threshold - items_total
    else:
        delivery = 0
        amount_to_spend = 0

    grand_total = items_total + delivery

    # Shopping Basket context data
    context = {
        'basket_items': basket_items,
        'items_count': items_count,
        'items_total': items_total,
        'standard_delivery': standard_delivery,
        'delivery': delivery,
        'amount_to_spend': amount_to_spend,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
