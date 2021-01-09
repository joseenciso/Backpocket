from django.apps import AppConfig


# Importing the signals module

class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """ Overiding the ready method """
        """ This signal will call the total model method
            every time a line item is saver or deleted """
        import checkout.signals
