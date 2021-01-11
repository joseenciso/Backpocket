from django.http import HttpResponse


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
        
        return HttpResponse(
            content=f'Webhook received: { event["type"] }',
            status=200,
        )
    
    def handle_payment_intent_payment_failed(self, event):
    """ handler payment_intent.payment_failed webhook from Stripe """
    return HttpResponse(
        content=f'Webhook received: { event["type"] }',
        status=200,
    )
