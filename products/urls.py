from django.urls import path
from . import views # We did not use 'import views' because views is a convention and might use a different views


urlpatterns = [
    path('', views.index),
    path('new/', views.new1)

]