from django.shortcuts import render

# Create your views here.


def view_shopping_bag(request):
    """ A view ehich renders our shopping bag """
    return render(request, 'bag/shopping_bag.html')
