from django.urls import path
from core.views import *
from product.views import *

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
]