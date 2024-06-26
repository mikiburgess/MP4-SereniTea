"""
    Profiles --> views.py
    - Adapted from Boutique Ado
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required(login_url="/accounts/login/")
def profile(request):
    """ Display the profile for the user """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Handle POST - user requests profile to be updated
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request,
                           'Profile update failed. Please check the form.')

    # Handle GET - user request to view their profile details
    form = UserProfileForm(instance=profile)  # populate from user profile
    orders = profile.orders.all().order_by("date").reverse()

    template = "profiles/profile.html"
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required(login_url="/accounts/login/")
def order_history(request, order_number):
    """ Display full order history for current user """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number[:6]}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
