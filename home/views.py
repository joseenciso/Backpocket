import random
import os
from django.shortcuts import render, get_object_or_404
from products.models import Product, Category, Sub_Category, Articles, Gender
from django.db.models import Q


def index(request):
    """ A view to return the index page """
    item = ''
    dic = {}

    #men_products = Gender.objects.all()
    #men_products = Products
    #print(men_products)
    #for prod in men_products:
    #    print(prod)

    GOOGLE_MAPS_KEY = os.environ.get('GOOGLE_MAPS_KEY')
    
    prev_prod = None
    product_count = Product.objects.count()
    for i in range(13):
        # Run a QUERY to count all the products in the DB
        # If products > 0 then rund randint 1, QUERY
        #print(i)
        product = Product.objects.get(pk=random.randint(1, product_count))
        #print(product)
        if product == prev_prod:
            -i
        else:
            dic["item{0}".format(i)] = product
            item+str(i)
        prev_prod = product
        # Else No products --> Message: No products Availabe <--
        # Defensive Design
    article_count = Articles.objects.count()
    article_name = Articles.objects.get(pk=random.randint(1, article_count))
    articles = Product.objects.filter(articles=article_name)
    print(articles)
    # articles_total = articles.count()
    
    category_count = Category.objects.count()
    category_name = Category.objects.get(pk=random.randint(1, category_count))
    categories = Product.objects.filter(categories=category_name)

    gender_count = Gender.objects.count()
    print(gender_count)
    gender_name = Gender.objects.get(pk=random.randint(2, gender_count))
    print(gender_name)
    gender_products = Product.objects.filter(gender=gender_name)
    print(gender_products)
    print(gender_products.count())

    context = {
        'GOOGLE_MAPS_KEY': GOOGLE_MAPS_KEY,
        'article_name': article_name.friendly_name,
        'articles': articles,
        'category_name': category_name.friendly_name,
        'categories': categories,
        'gender_name': gender_name.friendly_name,
        'gender_products': gender_products,
    }
    context.update(dic)
    #context.update(articles)
    #print(context)
    return render(request, 'home/index.html', context)

