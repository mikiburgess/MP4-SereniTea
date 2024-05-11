"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Basket app URLs for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]
