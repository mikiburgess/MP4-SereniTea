"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Reviews app VIEWS for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .models import UserProfile
from .models import Product

from .forms import ReviewForm


@login_required(login_url="/accounts/login/")
def my_reviews(request):
    """ Display full order history for current user """
    profile = get_object_or_404(UserProfile, user=request.user)
    reviews = Review.objects.all().filter(user_profile=profile)

    template = "reviews/my_reviews.html"
    context = {
        'reviews': reviews,
    }    
    return render(request, template, context)


@login_required(login_url="/accounts/login/")
def review_product(request, product_id):
    """ Write a review for a store product """
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # Handle POST requests
    if request.method == 'POST':

        print('--------')
        print(product.name)
        print(profile)
        print('--------')

        form = ReviewForm(request.POST)
    
        if form.is_valid():
            form.save()
            messages.success(request, 'Product review successfully submitted for approval.')
            # context = {
            #     'product': product,
            #     }
            return redirect(reverse('my_reviews'))
            # return render(request, 'products/product_detail.html', context)
        else:
            messages.error(request, 'Failed to submit review. Please check \
                           the form is valid.')
    else:
        # Handle GET requests
        form = ReviewForm()
        messages.info(request, f'You are reviewing {product.friendly_name}')
        template = 'reviews/review_product.html'
        context = {
            'form': form,
            'product': product,
            'user_profile': profile,
        }

    return render(request, template, context)
