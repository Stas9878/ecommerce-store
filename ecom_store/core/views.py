from django.shortcuts import render
from django.db.models import Q
from product.models import Product, Category


def frontpage(request):
    products = Product.objects.all()[:8]
    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    return render(request, 'core/signup.html')

def login(request):
    return render(request, 'core/login.html')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    #Активная категория
    active_cat = request.GET.get('category', '')
    if active_cat:
        products = products.filter(category__slug=active_cat)

    #Поиск
    query = request.GET.get('query', '')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_cat': active_cat,
    }
    return render(request, 'core/shop.html', context=context)
