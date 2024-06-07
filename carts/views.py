from django.shortcuts import render, redirect
from store.models import Product
from carts.models import Cart, CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import math
# Create your views here.




def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    
    print(f"cart id | session id(key): {cart}") # for testing purpose
    
    return cart



def add_to_cart(request, product_id):
    product = Product.objects.get(product_id=product_id) # get the product using product id

    print(f"Product Name: {product.product_name}") #for testing purpose


    try:
        cart = Cart.objects.get(
            cart_id = _cart_id(request)
        ) # get the cart id using present in session

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    print(f"Cart Id: {cart}") # for testing purpose


    try:
        cart_item = CartItem.objects.get(
            product = product,
            cart = cart
        )

        cart_item.quantity += 1
        
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        
        cart_item.save()

    # return HttpResponse(cart_item.product)

    return redirect("cart")



def remove_cart(request, product_id):

    product = Product.objects.get(product_id=product_id)

    cart = Cart.objects.get(cart_id=_cart_id(request))

    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    
    else:
        cart_item.delete()
    
    print(f"cart item: {cart_item.quantity}")

    return redirect("cart")



def remove_cart_item(request, product_id):

    product = Product.objects.get(product_id=product_id)

    cart = Cart.objects.get(cart_id=_cart_id(request))

    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item:
        cart_item.delete()

    return redirect("cart")


def cart(request, total=0, quantity=0, cart_items=None):

    try:
        cart = Cart.objects.get(
            cart_id = _cart_id(request)
        )

        cart_items = CartItem.objects.filter(
            cart = cart,
            is_active = True
        )

        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity


    except ObjectDoesNotExist:
        pass

    tax = total * (18 / 100)
    
    grand_total = total + tax
    
    
    context = {
        "total": total,
        "quantity" : quantity,
        "cart_items": cart_items,
        "tax": tax,
        "grand_total": grand_total
    }

    return render(request, 'store/cartPage.html', context)