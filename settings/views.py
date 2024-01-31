from django.shortcuts import render

from products.models import Product, Brand, Review

from django.db.models.aggregates import Count

from .models import Settings

# Create your views here.

def home(request):
    new_products = Product.objects.filter(flag='NEW')[:10]
    sale_products = Product.objects.filter(flag='SALE')[:10]
    feature_products = Product.objects.filter(flag='FEATURE')[:6]
    brands = Brand.objects.annotate(product_count=Count('product_brand'))[:10]
    reviews = Review.objects.all()[:6]
    settings_data = Settings.objects.last()

    print("\n\n*********************************\n")
    for r in reviews:
        print(r.rate)
    print("\n\n*********************************\n")
    
    return render(request, 'settings\home.html', {
        'new_products': new_products,
        'sale_products': sale_products,
        'feature_products': feature_products,
        'brands': brands,
        'reviews': reviews,
    })
