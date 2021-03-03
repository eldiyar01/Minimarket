from django.shortcuts import render

from .models import *


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products, 'categories': categories})


def category_products(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(id=pk)
    return render(request, 'products/category_products.html', {'categories': categories, 'category': category})


def product_detail(request, pk):
    categories = Category.objects.all()
    product = Product.objects.get(id=pk)
    return render(request, 'products/product.html', {'product': product, 'categories': categories})


def buy(request):
    pk = request.GET.get('pk')
    product = Product.objects.get(id=int(pk))
    return render(request, 'products/buy.html', {'product': product})


def search(request):
    categories = Category.objects.all()
    inp = request.GET.get('input')
    products = Product.objects.filter(name__icontains=inp)
    return render(request, 'products/home.html', {'search_products': products, 'categories': categories})
