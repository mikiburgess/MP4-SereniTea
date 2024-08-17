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
    """ Display all reviews submitted by current user """
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
    template = 'reviews/review_product.html'
    
    if request.method == 'POST':
        # Handle POST requests
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product review successfully submitted for approval.')        
        else:
            messages.error(request, 'Failed to submit review. Please check \
                           the form is valid.')
        context = {
            'product': product,
        }
        return render(request, 'products/product_detail.html', context)
    
    else:
        # Handle GET requests
        form = ReviewForm(initial={'user_profile': profile, 'product': product})
        messages.info(request, f'You are reviewing {product.friendly_name}')
        template = 'reviews/review_product.html'
        context = {
            'form': form,
            'product': product,
            'user_profile': profile,
        }
        return render(request, template, context)


@login_required(login_url="/accounts/login/")
def edit_review(request, rev_code):
    """ Edit a previously written product review """
    review = Review.objects.filter(review_code=rev_code).first()
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'reviews/edit_review.html'

    if request.method == 'POST':
        # Handle POST requests
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product review successfully updated.')
        else:
            messages.error(request, 'Failed to update product review.')       
        reviews = Review.objects.all().filter(user_profile=profile)
        template = "reviews/my_reviews.html"
        context = {
            'reviews': reviews,
        }    
        return render(request, template, context)
    else:
        # Handle GET requests
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing your product review')
        template = 'reviews/edit_review.html'
        context = {
            'form': form,
            'review': review,
            'user_profile': profile,
        }
    return render(request, template, context)
