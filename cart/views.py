from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Cart, CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # cart, created = Cart.objects.get_or_create(request.user, 1)[0]
    cart, created = Cart.objects.get_or_create(user=request.user)
    # cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)[0]
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    # return redirect('cart_detail')
    # return redirect('cart:cart_detail')
    response_data = {
        'message': 'Cart item created successfully.',
        'cart_size': cart.cartitem_set.count(),
    }
    return JsonResponse(response_data)


def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    # cart = CartItem.objects.all()
    return render(request, 'cart_detail.html', {'cart': cart})
