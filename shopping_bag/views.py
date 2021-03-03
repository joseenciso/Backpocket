from django.shortcuts import (render, redirect, reverse,
                            HttpResponse, HttpResponse,
                            get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_shopping_bag(request):
    """ A view which renders the shopping bag """
    return render(request, 'bag/shopping_bag.html')


def view_add_to_bag(request, product_pk):
    """
        A view to add quantities of the selected product
        to added to the shopping bag.
    """
    product = get_object_or_404(Product, pk=product_pk)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    bag = request.session.get('bag', {})
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    if size:
        if product_pk in list(bag.keys()):
            if size in bag[product_pk]['items_by_size'].keys():
                bag[product_pk]['items_by_size'][size] += quantity
                messages.success(request, f'Size updated for { product.name } to { bag[product_pk]["items_by_size"][size] }')
            else:
                bag[product_pk]['items_by_size'][size] = quantity
                messages.success(
                    request, f'{product.name} with the size of { size.upper() } added')
        else:
            bag[product_pk] = {'items_by_size': { size: quantity }}
            messages.success(request, f'{ product.name } with the size of  { size.upper() } added')
    else:
        if product_pk in list(bag.keys()):
            bag[product_pk] += quantity
            messages.success(request, f'{product.name} quantity updated to {bag[product_pk]}')
        else:
            bag[product_pk] = quantity
            messages.success(request, f'{product.name} added to the bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def view_edit_bag(request, product_pk):
    """ A view to edit/modify the shopping bag """
    product = get_object_or_404(Product, pk=product_pk)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})
    if size:
        if quantity > 0:
            bag[product_pk]['items_by_size'][size] = quantity
            messages.success(
                request, f'Size updated for { product.name } to { bag[product_pk]["items_by_size"][size] }')
        else:
            del bag[product_pk]['items_by_size'][size]['quantity'][quantity]
            if not bag[product_pk]['items_by_size']['quantity']:
                bag.pop(bag)
            messages.success(
                request, f'{product.name}, size { size.upper() } removed')
    else:
        if quantity > 0:
            bag[product_pk] = quantity
            messages.success(
                request, f'{product.name} quantity updated to { bag[product_pk] }')
        else:
            bag.pop(product_pk)
            messages.success(
                request, f'{ product.name } removed from the bag')
    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def view_remove_from_bag(request, product_pk):
    """ A view that delete an item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=product_pk)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})
        if size:
            del bag[product_pk]["items_by_size"][size]
            if not bag[product_pk]['items_by_size']:
                bag.pop(product_pk)
            messages.success(
                request, f'{product.name}, size {size.upper()} removed')
        else:
            bag.pop(product_pk)
            messages.success(
                request, f'{product.name} removed from the bag')
        request.session['bag'] = bag
        return redirect(reverse('shopping_bag'))
        # return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
