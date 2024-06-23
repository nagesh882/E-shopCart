from django.shortcuts import render, redirect
from store.models import Product, Variation
from carts.models import Cart, CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import math
# Create your views here.




def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    
    # print(f"cart id | session id(key): {cart}") # for testing purpose
    
    return cart



def add_to_cart(request, product_id):

    product = Product.objects.get(product_id=product_id) # get the product using product id
    product_variations = []


    if request.method == "POST":
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                product_variations.append(variation)
            except:
                pass


    # print(f"Product Name: {product.product_name}") #for testing purpose


    try:
        cart = Cart.objects.get(
            cart_id = _cart_id(request)
        ) # get the cart id using present in session

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    # print(f"Cart Id: {cart}") # for testing purpose


    is_cart_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_exists:
        cart_item = CartItem.objects.filter(
            product = product,
            cart = cart
        )
        # existing_variations -> database 
        # current variation -> product_variation
        # item_id -> database
        ex_var_list = []
        carts_id = []
        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation))
            carts_id.append(item.cart_item_id)

        print(ex_var_list)

        if product_variations in ex_var_list:
            # increase the cart item quantity
            index = ex_var_list.index(product_variations)
            item_id = carts_id[index]
            iteam = CartItem.objects.get(product=product, cart_item_id=item_id)
            iteam.quantity += 1
            iteam.save()

        else:
            # create new cart item
            item = CartItem.objects.create(product=product, quantity=1, cart=cart)


            if len(product_variations) > 0:
                item.variations.clear()
                item.variations.add(*product_variations)
                # cart_item.quantity += 1
            item.save()

    else:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        if len(product_variations) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variations)
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
    
    # print(f"cart item: {cart_item.quantity}")

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
        "tax": math.ceil(tax), # tax value shoud be round of
        "grand_total": math.ceil(grand_total)  # grand total value should be 
    }

    return render(request, 'store/cartPage.html', context)