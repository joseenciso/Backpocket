from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_shopping_bag(request):
    """ A view which renders the shopping bag """
    return render(request, 'bag/shopping_bag.html')


def view_add_to_bag(request, product_pk):
    """ A view to add quantities of the selected product to added to the shopping bag """
    product = get_object_or_404(Product, pk=product_pk)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    total_product = quantity
    
    size = None
    bag = request.session.get('bag', {})
    print("20", bag)
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
    if size:
        if product_pk in list(bag.keys()):
            print("26-PK", product_pk, "S",  size)
            if size in bag[product_pk]['items_by_size'].keys():
                bag[product_pk]['items_by_size'][size] += quantity
                messages.success(request, f'PAM1 Size updated for {product.name} to {bag[product_pk]["items_by_size"][size]}')
            else:
                bag[product_pk]['items_by_size'][size] = quantity
                messages.success(
                    request, f'PAM2{product.name} with the size of {size.upper()} added')
        else:
            bag[product_pk] = {'items_by_size': {size: quantity}}
            messages.success(request, f'PAM3{product.name} with the size of {size.upper()} added')
    else:
        if product_pk in list(bag.keys()):
            bag[product_pk] += quantity
            messages.success(request, f'PAM4{product.name} quantity updated to {bag[product_pk]}')
        else:
            bag[product_pk] = quantity
            messages.success(request, f'PAM5{product.name} added to the bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def view_edit_bag(request, product_pk):
    """ A view to edit/modify the shopping bag """
    product = get_object_or_404(Product, pk=product_pk)
    print("55", product)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
        print("57", size)

    bag = request.session.get('bag', {})

    if size:
        print("65", size)
        if quantity > 0:
            bag[product_pk]['items_by_size'][size] = quantity
            print("65", bag)
            messages.success(
                request, f'PAM1 Size updated for {product.name} to {bag[product_pk]["items_by_size"][size]}')
        else:
            print("69", bag)
            del bag[product_pk]['items_by_size'][size]['quantity'][quantity]
            print("71")
            if not bag[product_pk]['items_by_size']['quantity']:
                print("73")
                bag.pop(bag)
            messages.success(
                request, f'PAM2{product.name}, size {size.upper()} removed')
    else:
        print("78")
        if quantity > 0:
            print("80", quantity)
            bag[product_pk] = quantity
            print("82 - MERGED ITEMS")
            messages.success(
                request, f'PEM3 {product.name} quantity updated to {bag[product_pk]}')
        else:
            print("84", quantity)
            bag.pop(product_pk)
            messages.success(
                request, f'PEM4 {product.name} removed from the bag')
    request.session['bag'] = bag
    print("89", bag)    
    return redirect(reverse('shopping_bag'))


def view_remove_from_bag(request, product_pk):
    """ A view that delete an item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=product_pk)
        size = None
        print("99", product)
        if 'product_size' in request.POST:
            size = request.POST['product_size']
            print("102", size)

        bag = request.session.get('bag', {})
        print("107", bag)
        if size:
            print("109", size)
            print("109", bag)
            del bag[product_pk]["items_by_size"][size]
            print("111", bag)
            if not bag[product_pk]['items_by_size']:
                print("113", bag)
                bag.pop(bag)
                print("116", bag)
                #del bag[product_pk]["items_by_size"]
                print("115", bag)
            messages.success(
                request, f'PRM1 {product.name}, size {size.upper()} removed')
        else:
            print("117", bag)
            bag.pop(product_pk)
            messages.success(
                request, f'PRM2 {product.name} removed from the bag')
            
        request.session['bag'] = bag
        print("123", bag)
        return redirect(reverse('shopping_bag'))

        #return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
