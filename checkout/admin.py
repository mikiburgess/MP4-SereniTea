"""
Admin panel elements for Order & Orderline Models 
- - - - - - - - - - - - - - - - - - - -
"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmin,)

    readonly_fields = ('date',
                       'order_number',
                       'order_total',
                       'delivery_cost',
                       'grand_total',
                       'original_basket',
                       'stripe_pid',)

    fields = ('date',
              'order_number',
              'full_name',
              'email',
              'phone_number',
              'street_address1',
              'street_address2',
              'town_or_city',
              'county',
              'postcode',
              'country',
              'order_total',
              'delivery_cost',
              'grand_total',
              'original_basket',
              'stripe_pid',)

    list_display = ('order_number',
                    'date',
                    'full_name',
                    'order_total',
                    'delivery_cost',
                    'grand_total',)

    ordering = ('-date', '-full_name',)


admin.site.register(Order, OrderAdmin)
