from django.urls import path
from . import views # We did not use 'import views' because views is a convention and might use a different views
from .views import add_to_cart, cart_detail

app_name = 'cart'


urlpatterns = [
    # path('', views.index),
    # path('', views.cart_detail), 
    # path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), 
    path('cart/', views.cart_detail, name='cart_detail'),
]
