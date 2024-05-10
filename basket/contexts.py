"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Context Processor for the Basket App
- - - - - - - - - - - - - - - - - - - -
"""
from django.conf import settings


def basket_contents(request):
    # Initialise shopping basket and initial costs
    basket_items = []
    items_count = 0
    items_total = 0
    standard_delivery = settings.STANDARD_DELIVERY_CHARGE
    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD

    # Calculate current costs and delivery charge
    if 0 < items_total < free_delivery_threshold:
        delivery = standard_delivery
        amount_to_spend = free_delivery_threshold - items_total
    else:
        delivery = 0
        amount_to_spend = 0

    grand_total = delivery + items_total

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
