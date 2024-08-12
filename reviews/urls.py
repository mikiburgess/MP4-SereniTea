"""
Review app URLs for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.urls import path
from . import views


urlpatterns = [
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('review_product/<int:product_id>/', views.review_product, name='review_product'),
    # path('product_reviews/<int:product_id>/', views.product_reviews, name='product_reviews'),
    # path('edit_review/<int:review_code>/', views.edit_review, name='edit_review'),
    # path('delete_review/<int:review_code>/', views.delete_review, name='delete_review'),
]
