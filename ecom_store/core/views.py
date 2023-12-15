from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from product.models import Product, Category
from .forms import SignUpForm


def frontpage(request):
    products = Product.objects.all()[:8]
    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('core:myaccount')

    return render(request, 'core/edit_myaccount.html')


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
