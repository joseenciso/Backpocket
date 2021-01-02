import random
from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()

    item1 = Product.objects.get(pk=randNumber())
    item2 = Product.objects.get(pk=randNumber())
    item3 = Product.objects.get(pk=randNumber())
    item4 = Product.objects.get(pk=randNumber())

    context = {
        'products': products,
        'item1': item1,
        'item2': item2,
        'item3': item3,
        'item4': item4,
    }

    # print(products)
    return render(request, 'home/index.html', context)


def randNumber():
    rand = random.randint(0, 40)
    # print(rand)
    return rand
