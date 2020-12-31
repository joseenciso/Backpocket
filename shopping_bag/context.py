from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_context(request):

    # Empty list bag container
    bag_items = []
    delivery = 0

    # Initializing total and products count
    total = 0
    products_count = 0

    bag = request.session.get('bag', {})
    for product_pk, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_pk)
        total += quantity * product.price
        products_count += quantity
        bag_items.append({
            'product_pk': product_pk,
            'quantity': quantity,
            'product': product,
            'total': total,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Decimal is prefer for money because it is more accurate
        deliver = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery = 0

    grand_total = delivery + total

    # returning a dictionary rather than a view
    # Context processor
    context = {

        'bag_items': bag_items,
        'products_count': products_count,
        'total': total,
        'delivery': delivery,
        'free_delivery': free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
