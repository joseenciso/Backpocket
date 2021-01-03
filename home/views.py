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
    item5 = Product.objects.get(pk=randNumber())
    item6 = Product.objects.get(pk=randNumber())
    item7 = Product.objects.get(pk=randNumber())
    item8 = Product.objects.get(pk=randNumber())
    item9 = Product.objects.get(pk=randNumber())
    item10 = Product.objects.get(pk=randNumber())
    item11 = Product.objects.get(pk=randNumber())
    item12 = Product.objects.get(pk=randNumber())

    rand_product1 = Product.objects.get(pk=randNumber())

    context = {
        'products': products,
        'item1': item1,
        'item2': item2,
        'item3': item3,
        'item4': item4,
        'item5': item5,
        'item6': item6,
        'item7': item7,
        'item8': item8,
        'item9': item9,
        'item10': item10,
        'item11': item11,
        'item12': item12,
        'rand_product1': rand_product1,
    }

    # print(products)
    return render(request, 'home/index.html', context)


def randNumber():
    rand = random.randint(1, 40)
    # print(rand)
    return rand
