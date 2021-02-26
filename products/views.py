from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # to generate a seach query
from django.db.models.functions import Lower
from .models import Product, Category, Articles, Gender
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
            category = request.GET['categories']
            print("42-C: ", category, "\n")
            # Creating a list
            #categories = categories.filter(categories__in=categories)
            # categories = Category.objects.filter(category_name__in=catgories)
            all_categories = Category.objects.all()
            print("47-C: ", all_categories, "\n")
            categories = Category.objects.filter(name__in=category)
            print("48-C: ", categories, "\n")
            for cat in categories:
                print(cat)

        if 'gender' in request.GET:
            gender_all = Gender.objects.all()
            print("56-", gender_all)
            gender = request.GET['gender']
            print("56-G: ", gender)
            # print(products.filter(gender__in=gender))
            products = products.filter(gender__name=gender)
            print("59-G: ", products)
            # for g1 in gend:
            #    print("g1", g1)
            # gender1 = Product.objects.filter(gender__name=gender)
            # print("61", gender1)
            # for g2 in gender1:
            #    print("g2", g2)

        # if 'type' in request.GET:
        #    article = request.GET['categories'].split(',')
            # Creating a list
        #     products = products.filter(categories__in=categories)

        if 'q' in request.GET:  # q for Query
            query = request.GET['q']
            if not query:  # If query is blank
                messages.warning(request, "Looks like you didn't enter any serch critiria")
                #print(messages.error(request, "You didn't enter any serch critiria"))
                return redirect(reverse('allproducts'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            # the i makes the queries case insensitive
            products = products.filter(queries)
    # print("76 - Q: ", query)
    current_sort = f'{sort}_{direction}'
    #rating = products.filter()
    # print(products)
    # print("CS: ", current_sort)

    total_products = products.count()
    # Future Feature
    # p = Paginator(products, 7)
    # print("p", p)
    # page_num = request.GET.get('page', 1)

    # try:
    #    page = p.page(page_num)
    # except EmptyPage:
    #    page = p.page(1)
    # print(p, page, page.count,  page_num)

    context = {
        'total_products': total_products,
        'products': products,
        'search_term': query,
        'current_category': categories,
        'current_sort': current_sort,
    }

    # print(query)
    return render(request, 'products/allproducts.html', context)


def product(request, pk):
    """ A view to show a products detail """
    product = get_object_or_404(Product, pk=pk)
    print(product)
    print(pk)

    #suggestions = 

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
