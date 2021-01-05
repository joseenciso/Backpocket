from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_context(request):

    # Empty list bags container
    bag_items = []
    bag = request.session.get('bag', {})

    delivery = 0
    total = 0
    product_count = 0
    size = None

    for product_pk, product_data in bag.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_pk)
            total += product_data * product.price
            product_count += product_data
            bag_items.append({
                'product_pk': product_pk,
                'quantity': product_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_pk)
            for size, quantity in product_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'product_pk': product_pk,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
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
        'products_count': product_count,
        'total': total,
        'delivery': delivery,
        'free_delivery': free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
