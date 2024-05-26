"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Home app URLs for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_serenitea', views.about_serenitea, name='about_serenitea'),
    path('shipping', views.shipping, name='shipping'),
]
