from django.urls import path
from django.contrib.auth.views import LoginView
from product.views import *
from .views import *

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    #user auth
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    #account
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    #shop
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
]