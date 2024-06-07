from django.shortcuts import render
from store.models import Product
from category.models import Category
from django.core.paginator import Paginator
from carts.models import Cart, CartItem
from carts.views import _cart_id
from django.http import HttpResponse
# Create your views here.


def storePage(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None:
        categories = Category.objects.get(category_slug=category_slug)
        
        products = Product.objects.filter(category=categories, is_availabel=True)

        paginator = Paginator(products, 1)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number) 

        product_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_availabel=True).order_by('product_id')

        paginator = Paginator(products, 3)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number) 
        
        product_count = products.count()

    context = {
        "products": products,
        "page_object" : page_object,
        "product_count": product_count
    }

    print("=" * 100)
    print(f"Product Names: {[ product.product_name for product in products ]}")
    print("*"*100)
    print(f"Total Product Count: {product_count}")
    print("*"*100)
    print(f"Page Object: {page_object}")
    print("=" * 100)

    return render(request, 'store/storePage.html', context)



def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__category_slug=category_slug, product_slug=product_slug)

        product_in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e

    print("=" * 100)
    print(f"Product Name: {single_product.product_name}")
    print("=" * 100)

    context = {
        "single_product": single_product,
        "product_in_cart":product_in_cart   
    }

    return render(request, "store/product_detail.html", context)