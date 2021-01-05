from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    model = Order
    fields = ('full_name', 'email', 'order_number', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'country', 'postcode', 'county',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and class, remove auto-generated labels and set autofocus on first field """

        super().__init__(*args, ***kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Post Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address1': 'Street Andress 2',
            'county': 'COunty',
        }

    self.fields['full_name'].widget.attrs['autofocus'] = True
