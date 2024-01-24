from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


# def new1(request):
#     return HttpResponse("NEW PRODUCTS")


# def index(request):
#     # return render(request, "index.html")
#     return HttpResponse("Hello, world. You're at the products index.")

# def new1(request):
#     return HttpResponse("NEW PRODUCTS")