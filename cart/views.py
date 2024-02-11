# import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum


from .models import Cart, CartItem
from products.models import Product
from products.views import index


def add_to_cart(request, pk):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=pk)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product:home')

def remove_from_cart(request, pk):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=pk)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
        # return redirect('cart:cartdetail')
    return redirect('product:home')


def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    count = cart.cartitem_set.all().aggregate(Sum('quantity'))['quantity__sum']
    return render(request, 'cart_detail.html', {'cart': cart, 'count': count})



# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     # cart, created = Cart.objects.get_or_create(request.user, 1)[0]
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     # cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)[0]
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     # return redirect('cartdetail')
#     # return redirect('cart:cartdetail')
#     response_data = {
#         'message': 'Cart item created successfully.',
#         'cart_size': cart.cartitem_set.count(),
#     }
#     return JsonResponse(response_data)


# def cart_detail(request):
#     cart = Cart.objects.get(user=request.user) 
#     # cart = CartItem.objects.all()
#     # cart_count =request.session.get('cart_count', 0)
#     count_items = CartItem.objects.aggregate(total=Sum('quantity'))
#     return render(request, 'cart_detail.html', {'cart': cart, "count_items": count_items['total'] - 1})
