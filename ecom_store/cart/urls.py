from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('<int:product_id>/', add_to_cart, name='add_to_cart')
]