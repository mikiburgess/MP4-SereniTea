"""
Product Views for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # to generate search queries in Django
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


# Product app views

def all_products(request):
    """ View to show all products """
    print(request)
    products = Product.objects.all()  # retrieve all products from database
    categories = None  # initialise current selected product categories to None (i.e. unspecified)
    group = None  # initialise current selected product group to None (i.e. unspecified)
    sort = None  # initialise product sorting element to None (i.e. unspecified)
    direction = None  # initialise product sorting order to None (i.e. unspecified)
    query = None  # initialise query search term to None (i.e. unspecified)

    if request.GET:
        # Handle user submitting a sort request
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        # Handle user submitting search request
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            # Filter if search term present in product name OR product description OR image description
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(alt_text__icontains=query)
            products = products.filter(queries)

        # Handle user submitting request to view products in specific category
        if 'category' in request.GET:
            print(f'Request: {request}')
            categories = request.GET['category'].split(',')  # allow for multiple categories
            print(f'Categories: {categories}')
            products = products.filter(category__name__in=categories)
            print(f'Products: {products}')
            # get category objects to enable access to category fields
            categories = Category.objects.filter(name__in=categories)
            print(f'Categories: {categories}')

        # Handle user submitting request to view all products in a specific category group
        if 'group' in request.GET:
            group = request.GET['group']
            print(f'Group: {group}')
            # obtain all Category objects where Category.group = requested group
            categories = Category.objects.filter(group__iexact=group)
            print(f'Categories: {categories}')
            # iterate through the group categories to extract list of category names
            names = []
            for category in categories:
                names.append(category.name)
            # filter products based on category name
            products = products.filter(category__name__in=names)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_sorting': current_sorting,
        'current_group': group,
        'current_categories': categories,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to show details of individual products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required(login_url="/accounts/login/")
def add_product(request):
    """ Add a new product to the store """
    # Check user has permission to access this feature
    if not request.user.is_superuser:
        messages.error(request,
                       'Oops! You are not authorized to access that page.')
        return redirect(reverse('home'))

    # Handle POST requests
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request,
                             'New product successfully added to store catalogue.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product. Please check the form is valid.')
    else:
        # Handle GET requests
        form = ProductForm()
        template = 'products/add_product.html'
        context = {
            'form': form,
        }

    return render(request, template, context)


@login_required(login_url="/accounts/login/")
def edit_product(request, product_id):
    """ Update details of an existing store product """
    # Check user has permission to access this feature
    if not request.user.is_superuser:
        messages.error(request,
                       'Oops! You are not authorized to access that page.')
        return redirect(reverse('home'))

    # retrieve details of the selected product
    product = get_object_or_404(Product, pk=product_id)
    # Handle POST requests
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Product successfully updated in store catalogue.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product. Please ensure the form is valid.')
    else:
        # Handle GET requests
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.friendly_name}')
        template = 'products/edit_product.html'
        context = {
            'form': form,
            'product': product,
        }

    return render(request, template, context)


@login_required(login_url="/accounts/login/")
def delete_product(request, product_id):
    """ Delete a product from the store catalogue """
    # Check user has permission to access this feature
    if not request.user.is_superuser:
        messages.error(request,
                       'Oops! You are not authorized to access that page.')
        return redirect(reverse('home'))

    # retrieve details of the selected product
    product = get_object_or_404(Product, pk=product_id)
    # Delete product from database
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect(reverse('products'))
