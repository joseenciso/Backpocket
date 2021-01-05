import random
from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()
    item = ''
    dic = {}

    for i in range(1, 12):
        dic["item{0}".format(i)] = Product.objects.get(pk=randNumber())
        item+str(i)

    context = {}
    context.update(dic)
    return render(request, 'home/index.html', context)


def randNumber():
    rand = random.randint(1, 40)
    return rand
