from django.urls import path
from . import views # We did not use 'import views' because views is a convention and might use a different views
# from .views import add_to_cart, cart_detail

app_name = 'cart'


urlpatterns = [
    path('cartdetail/', views.cart_detail, name='cartdetail'),
    path('addcart/<int:pk>/', views.add_to_cart, name='addcart'), 
    path('removecart/<int:pk>/', views.remove_from_cart, name='removecart'),
]
    # # path('', views.index), 
    # # path('minicart/', views.mini_cart, name='minicart'), 
    # # path('', views.cart_detail), 
    # # path('add-to-cart/', add_to_cart, name='add_to_cart'),
    # path('cartdetail/', views.cart_detail, name='cartdetail'),
    # path('addcart/<int:product_id>/', views.add_to_cart, name='addcart'), 
