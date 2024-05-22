"""
Product Views for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
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

            # Filter if search term present in product name OR product description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # Handle user submitting request to view products in specific category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')  # allow for multiple categories
            products = products.filter(category__name__in=categories)
            # get category objects to enable access to category fields
            categories = Category.objects.filter(name__in=categories)

        # Handle user submitting request to view all products in a specific category group
        if 'group' in request.GET:
            group = request.GET['group']
            # obtain all Category objects where Category.group = requested group
            categories = Category.objects.filter(group__iexact=group)
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


def add_product(request):
    """ Add a new product to the store """
    # Handle POST requests
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New product successfully added to store catalogue.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please check the form is valid.')
    else:
        # Handle GET requests
        form = ProductForm()
        template = 'products/add_product.html'
        context = {
            'form': form,
        }

    return render(request, template, context)
