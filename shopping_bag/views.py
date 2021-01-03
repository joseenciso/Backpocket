from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponse

# Create your views here.


def view_shopping_bag(request):
    """ A view ehich renders our shopping bag """
    return render(request, 'bag/shopping_bag.html')


def view_add_to_bag(request, product_id):
    """ A view to add quantities of the selected product to added to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    # product_id = int(product_id)
    redirect_url = request.POST.get('redirect_url')
    total_product = quantity
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})
    print(bag)
    print(product_id)

    if size:
        # print(list(bag.keys()))
        if product_id in list(bag.keys()):
            if size in bag[product_id]['items_by_size'].keys():
                bag[product_id]['items_by_size'][size] += quantity
            else:
                bag[product_id]['items_by_size'][size] = quantity
        else:
            bag[product_id] = {'items_by_size': {size: quantity}}

            if product_id in list(bag.keys()):
                bag[product_id] += quantity
            else:
                bag[product_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def view_edit_bag(request, product_id):
    """ A view to edit/modify the shopping bag """
    quantity = int(request.POST.get('quantity'))

    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get['bag', {}]

    if size:
        if quantity > 0:
            bag[product_id]['items_by_size'][size] = quantity
        else:
            del bag[product_id]['items_by_size'][size]
            if not bag[product_id]['items_by_size']:
                bag.pop(bag)
    else:
        if quantity > 0:
            bag[product_id] = quantity
        else:
            bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def view_remove_from_bag(request, product_id):
    """ A view that delete an item from the shopping bag """
    size = None

    try:
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        bag = request.session.get['bag', {}]

        if size:
            del bag[product_id]['items_by_size'][size]

            if not bag[product_id]['items_by_size']:
                bag.pop(bag)
        else:
            bag.pop(product_id)

        request.session['bag'] = bag
        print(bag)
        # return redirect(reverse('view_shopping_bag'))

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
