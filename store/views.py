from django.shortcuts import render
from store.models import Product
# Create your views here.


def storePage(request):

    products = Product.objects.all().filter(is_availabel=True)

    product_count = products.count()

    context = {
        "products": products,
        "product_count": product_count
    }

    print(f"Product Names: {[ product.product_name for product in products ]}")
    print(f"Total Product Count: {product_count}")

    return render(request, 'store/storePage.html', context)