from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # to generate a seach query
from .models import Product
# Create your views here.


def all_products(request):
    """ A view to show all products """
    # import pdb;
    products = Product.objects.all()
    query = None
    category = None
    # print(products)
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')  # Creating a list
            products = products.filter(category__name__in=categories)

        if 'q' in request.GET:  # q for Query
            query = request.GET['q']
            if not query:  # If query is blank
                messages.error(request, "You didnt enter any serch critiria")
                print(messages)
                return redirect(reverse('allproducts'))

            queries = Q(product_name__icontains=query) | Q(
                description__icontains=query)
            # the i makes the queries case insensitive
            products = products.filter(queries)

        print(products)
    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/allproducts.html', context)


def product(request, pk):
    """ A view to show a products detail """
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'products/product.html', context)
