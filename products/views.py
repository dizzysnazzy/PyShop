from django.shortcuts import render
from django.db.models import Sum

from cart.models import Cart
from .models import Product, Offer
from cart.models import CartItem


def index(request):
    products = Product.objects.all()
    cart = Cart.objects.get(user=request.user)
    count = cart.cartitem_set.all().aggregate(Sum('quantity'))['quantity__sum']
    context = {'products': products, 'count': count}
    return render(request, "index.html", context)



    # count_items = CartItem.objects.aggregate(total=Sum('quantity'))
    # return render(request, "index.html", {"products": products, "count_items": count_items['total'] - 1})