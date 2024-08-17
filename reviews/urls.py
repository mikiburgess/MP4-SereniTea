"""
Review app URLs for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.urls import path
from . import views


urlpatterns = [
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('review_product/<int:product_id>/', views.review_product, name='review_product'),
    path('edit_review/<str:rev_code>/', views.edit_review, name='edit_review'),
    path('delete_review/<str:rev_code>/', views.delete_review, name='delete_review'),
]
