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

    readonly_fields = ('order_number',
                       'order_total',
                       'delivery_cost',
                       'grand_total',
                       'date',)

    fields = ('order_number',
              'title',
              'first_name',
              'surname',
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
              'date',)

    list_display = ('order_number',
                    'date',
                    'title',
                    'surname',
                    'order_total',
                    'delivery_cost',
                    'grand_total',)

    ordering = ('-date', '-surname', '-first_name',)


admin.site.register(Order, OrderAdmin)
