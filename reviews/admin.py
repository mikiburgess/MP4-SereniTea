"""
Reviews Administration for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.contrib import admin
from .models import Review

# Set up admin page for reviews
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'approved',
        'product',
        'date',
        'stars',
        'comment',
        'name',
        'user_profile',
        'review_code',
    )
    ordering = ('product', 'date',)

# Register Models
admin.site.register(Review, ReviewAdmin)
