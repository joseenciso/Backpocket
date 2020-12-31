from django.shortcuts import render, redirect

# Create your views here.


def view_shopping_bag(request):
    """ A view ehich renders our shopping bag """
    return render(request, 'bag/shopping_bag.html')


def view_add_to_bag(request, product_id):
    """ A view to add quantities of the selected product to added to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    total_product = quantity
    print(bag)

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def view_edit_bag(request, product_id):
    """ A view to edit/modify the shopping bag """
    quantity

    """ A view that delete an item from the shopping bag """
