from django.shortcuts import render
from store.models import Product
from category.models import Category
# Create your views here.


def storePage(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None:
        categories = Category.objects.get(category_slug=category_slug)
        
        products = Product.objects.filter(category=categories, is_availabel=True)

        product_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_availabel=True)

        product_count = products.count()

    context = {
        "products": products,
        "product_count": product_count
    }

    print(f"Product Names: {[ product.product_name for product in products ]}")
    print(f"Total Product Count: {product_count}")

    return render(request, 'store/storePage.html', context)