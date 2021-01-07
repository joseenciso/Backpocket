from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from shopping_bag.context import bag_context

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in our bag at the moment.")
        return redirect(reverse(''))

    current_bag = bag_context(request)

    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_LzQaIFacxKBEscQpKzHACBJA00XXhrHZ9M',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
