# Django imports
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Project imports
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

# Python libraries
import stripe
import json
import time


class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def _send_order_confirmation_email(self, order):
        """ Send the user a confirmation email upon order completion """
        print("\n Sending email ... \n")
        customer_email = order.email
        email_subject = render_to_string(
            'checkout/confirmation_emails/order_confirmation_email_subject.txt',
            {'order': order})
        email_body = render_to_string(
            'checkout/confirmation_emails/order_confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False,
        )

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

        #  Handle user profile in same way as in usual checkout process 
        #  Update profile information is user has checked the 'save_info' option
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default.full_name = shipping_details.name
                profile.default.email = billing_details.email
                profile.default.phone_number = shipping_details.phone
                profile.default.street_address1 = shipping_details.address.line1
                profile.default.street_address2 = shipping_details.address.line2
                profile.default.town_or_city = shipping_details.address.city
                profile.default.county = shipping_details.address.state
                profile.default.postcode = shipping_details.address.postal_code
                profile.default.country = shipping_details.address.country

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
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
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
                self._send_order_confirmation_email(order)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)
            else:
                order = None
                try:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        postcode=shipping_details.address.postal_code,
                        country=shipping_details.address.country,
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
        self._send_order_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Order created by webhook handler',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )
