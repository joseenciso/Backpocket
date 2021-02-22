import random
import os
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponse
from products.models import Product, Category, Sub_Category, Articles, Gender
from django.db.models import Q
from django.contrib import messages
from django.urls import get_resolver, get_urlconf, resolve, reverse, NoReverseMatch


def index(request):
    """ A view to return the index page """
    item = ''
    dic = {}
    GOOGLE_MAPS_KEY = os.environ.get('GOOGLE_MAPS_KEY')
    
    prev_prod = None
    product_count = Product.objects.count()
    for i in range(3):
        # Run a QUERY to count all the products in the DB
        # If products > 0 then rund randint 1, QUERY
        #print(i)
        try:
            pk = random.randint(1, product_count)
            product = get_object_or_404(Product, pk=pk)
            #print("ppk", pk, "p", product, product.pk)
        except (Exception, NoReverseMatch) as e:
            messages.error(request, f'NoReverseMatch on item {e}')
            #print("29-pe", e, product, product.pk)
            return HttpResponse(status=500)
        #pro_test = get_object_or_404(Product, pk=random.randint(1, product_count))
        #print(i,"\t", product.pk,"\t", pro_test,"\t")
        #print(product)
        #print("PT-L29", pro_test)
        if product == prev_prod:
            pk = random.randint(1, product_count)
            product = get_object_or_404(Product, pk=pk)
            #print("35 - P: ", product, "pv-p: ", prev_prod, "i - ", i)
            #i-=1
            #print("37", i)
            dic["item{0}".format(i)] = product
            item+str(i)
        else:
            #print("39", i)
            dic["item{0}".format(i)] = product
            item+str(i)
            #print("ITEM", item+str(i))
            #print("43-P", product)
        #print("43", i)
        prev_prod = product
        
        # Else No products --> Message: No products Availabe <--
        # Defensive Design
    
    try:
        article_count = Articles.objects.count()
        a_pk = random.randint(1, article_count)
        article_name = Articles.objects.get(pk=a_pk)
        articles = Product.objects.filter(articles=article_name)[:8]
        # articles_total = articles.count()
    except (Exception, NoReverseMatch) as e:
        print("55-ae", e, NoReverseMatch)
        

    try:
        category_count = Category.objects.count()
        c_pk = random.randint(1, category_count)
        category_name = Category.objects.get(pk=c_pk)
        categories = Product.objects.filter(categories=category_name)[:8]
    except (Exception, NoReverseMatch) as e:
        print("67-ce", e, NoReverseMatch)

    try:
        gender_count = Gender.objects.count()
        g_pk = random.randint(2, gender_count)
        gender_name = Gender.objects.get(pk=random.randint(2, gender_count))
        gender_products = Product.objects.filter(gender=gender_name)[:8]
    except (Exception, NoReverseMatch) as e:
        print("78-ge", e, NoReverseMatch)

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

