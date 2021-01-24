from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # to generate a seach query
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
# Create your views here.


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    category = None
    categories = None
    article_type = None
    gender = None
    sort = None
    direction = None
    rate = 0

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # products.order_by(category__name)
            products = products.order_by(sortkey)

        if 'categories' in request.GET:
            categories = request.GET['categories'].split(',')
            # Creating a list
            categories = categories.filter(categories__in=categories)
            # categories = Category.objects.filter(category_name__in=catgories)
            categories = Product.objects.filter(category_name__in=categories)

        # if 'gender' in request.GET:
        #    gender = request.GET['gender'].split(',')
            # Creating a list
        #    products = products.filter(gender__in=gender)

        # if 'type' in request.GET:
        #    article = request.GET['categories'].split(',')
            # Creating a list
        #     products = products.filter(categories__in=categories)

        if 'q' in request.GET:  # q for Query
            query = request.GET['q']
            if not query:  # If query is blank
                messages.error(request, "You didn't enter any serch critiria")
                print(messages.error(request, "You didn't enter any serch critiria"))
                return redirect(reverse('allproducts'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            # the i makes the queries case insensitive
            products = products.filter(queries)

    current_sort = f'{sort}_{direction}'
    rating = products.filter()
    # print(products)
    print(current_sort)

    context = {
        'products': products,
        'search_term': query,
        'current_category': categories,
        'current_sort': current_sort,
    }

    print(query)
    return render(request, 'products/allproducts.html', context)


def product(request, pk):
    """ A view to show a products detail """
    product = get_object_or_404(Product, pk=pk)
    print(product)
    print(pk)

    context = {
        'product': product,
    }

    return render(request, 'products/product.html', context)


@login_required
def add_new_product(request):
    """ View to add new products """
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            product = form.save()
            messages.success(request, f'Product added!')
            return redirect(reverse('product', arg=[product.pk]))
        else:
            messages.error(request, f'Couldnt add the product, please check every field before submitting.')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, pk):
    """ A view to edit an alredy existing product """
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILE, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated!')
            return redirect(reverse('product', arg=[product.pk]))
        else:
            messages.error(request, 'Failed to update the product! Please, double check the form fields.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are about to edit { product.name }')

    template = 'products/add_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, pk):
    """ View that will delete a product from our DB """
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, f'Product { product.name } successfully deleted!')
    return redirect(reverse('allproducts'))
