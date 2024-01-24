from django.urls import path, include
from . import views # We did not use 'import views' because views is a convention and might use a different views


urlpatterns = [
    path('', views.index),
    path('', include('cart.urls', namespace='cart')),
    # path('new/', views.new1),
]
