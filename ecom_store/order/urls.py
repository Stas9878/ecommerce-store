from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('start_order/', start_order, name='start_order'),
]