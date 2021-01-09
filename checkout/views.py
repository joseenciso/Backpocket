from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from shopping_bag.context import bag_context
import stripe

# Create your views here.


def checkout(request):
    # Stripe's payment intent
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    print("Method: ", request.method)
    print("POST? ", request.method == 'POST')
    if request.method == 'POST':
        print("POST?", request.method == 'POST')
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        print("Order Form: ", form_data )
        order_form = OrderForm(form_data)

        # print("Order Valid 1? ", order_form.is_valid())
        if order_form.is_valid():
            print("Order Valid 2? :", order_form.is_valid())
            order = order_form.save()
            for product_pk, product_data in bag.items():
                try:
                    product = Product.objects.get(pk=product_pk)
                    print("P-46: ", product)
                    if isinstance(product_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                        print("O_L_I-54: ", order_line_item)
                        order_line_item.save()
                    else:
                        for size, quantity in product_data['items_by_size'].items():
                            print("OLI-59", OrderLineItem)
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            print(order_line_item.order)
                            print(order_line_item.product)
                            print(order_line_item.product_size)
                            print(order_line_item.quantity)
                            print("O_L_I-64: ", order_line_item)
                            order_line_item.save()
                except Product.DoesNotExist:
                    message.error(request, ("One of the products not found!"))
                    order.delete()
                    print("Order Deleted. Return Shopping Bag")
                    return redirect(reverse('shopping_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            print(request.session['save_info'])
            print("Checkout Success")
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print("There is an erro in the form")
            messages.error(request, "There is an error in the form!")
        
    else:
        print("Else :", request.session.get('bag', {}))
        bag = request.session.get('bag', {})
        print("Bag 78: ", bag)
        if not bag:
            messages.error(request, "There is nothing in your bag at the moment.")
            print("There is nothing in the bag at the moment")
            return redirect(reverse('home'))

        current_bag = bag_context(request)
        total = current_bag['grand_total']

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print("Intent", intent)
        print("Order Form 95: ", OrderForm())
        order_form = OrderForm()

    if not stripe_public_key:
        print("No public key")
        messages.warning(request, 'Stripe public key misssing.')

    # print(stripe_total)
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    print("Last Line, back to checkout")
    return render(request, template, context)


def checkout_success(request, order_number):
    """ Success Checkout Handler """
    save_info = request.sessino.get('save_info')
    order = get_object_or_404(order, order_number=order_number)
    messages.success(request, f'Order { order_number } Successed!\
        We will send you the confirmation detail to { order.email }.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)





