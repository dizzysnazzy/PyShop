from django.urls import path, include
from . import views # We did not use 'import views' because views is a convention and might use a different views

app_name = 'product'


urlpatterns = [
    path('', views.index, name='home'),
    path('', include('cart.urls')),


    # path('', views.index, name='home'),
    # path('', include('cart.urls', namespace='cart')),
    # # path('new/', views.new1),
]
