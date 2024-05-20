"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Basket supplementary tools for "SERENITEA EMPORIUM"
- adapted from Boutique Ado
- - - - - - - - - - - - - - - - - - - -
"""
from django import template

register = template.Library()


# Link basket tool function to backet templates
@register.filter(name='calculate_line_subtotal')
def calculate_line_subtotal(price, quantity):
    return price * quantity
