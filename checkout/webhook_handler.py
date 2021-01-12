from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product

import json
import time

class StripeWH_Handler():
    """ Webhook Handler for Stripe """
    def __inin__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected event """
        return HttpResponse(
            content=f'Unhandle webhook received: { event["type"] }',
            status= 200,
        )
    
    def handle_payment_intent_succeeded(self, event):
        """ handler payment_intent.succeeded webhook from Stripe """
        intent = event.data.object
        payment_id = intent.id
        bag = intent.metadata.bag

        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_detailes
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount/100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        order_exist = False

        attempt = 1
        while attempt <= 5 :
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.address.country,
                    country__iexact=shipping_details.address.postal_code,
                    postcode__iexact=shipping_details.address.city,
                    town_or_city__iexact=shipping_details.address.line1,
                    street_address1__iexact=shipping_details.address.line2,
                    street_address2__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_payment_id=payment_id
                )
                order_exist = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        
        if order_exist:
            return HttpResponse(
                content=f'Webhook received: { event["type"] } | SUCCESS: Verified order, already in database',
                status=200,
            )
        else:
            order = None
            try:
                order = Order.Objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.address.country,
                    country=shipping_details.address.postal_code,
                    postcode=shipping_details.address.city,
                    town_or_city=shipping_details.address.line1,
                    street_address1=shipping_details.address.line2,
                    street_address2=shipping_details.address.state,
                    original_bag=bag,
                    stripe_payment_id=payment_id
                )
                for product_pk, product_data in json.loads(bag).items():
                    product = Product.objects.get(pk=product_pk)
                    if isinstance(product_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in product_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: { event["type"] } | ERROR: {e}', status=500)
            return HttpResponse(
                content=f'Webhook received: { event["type"] } | SUCCESS: Order created in webhooks',
                status=200,
            )


    def handle_payment_intent_payment_failed(self, event):
        """ handler payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: { event["type"] }',
            status=200,
        )
