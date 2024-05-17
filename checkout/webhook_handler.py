from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook from Stripe """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details (replace empty string with null)
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Check if order already exists
        order_exists = False
        # max 5 attempts to retrieve order, to allow for syncronisation issues
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    # iexact -> exact match but case insensitive
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.street_address1,
                    street_address2__iexact=shipping_details.address.street_address2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.county,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
            if order_exists:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)
            else:
                order = None
                try:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.street_address1,
                        street_address2=shipping_details.address.street_address2,
                        county=shipping_details.address.county,
                        original_basket=basket,
                        stripe_pid=pid,
                    )
                    for item_id, item_data in json.loads(basket).items():
                        product = Product.objects.get(id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Order created by webhook handler',
            status=200
        )

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )
