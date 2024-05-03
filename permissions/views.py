from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products
from .serializers import ProductsSerializer

def get_products():
    p = list(Products.objects.all())
    products = []
    for product in p:
        products.append(ProductsSerializer(product).data)
    print(products)
    return products

def create_products(request):
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    p = Products(title=title,desc=desc)
    # p.save()
    if(p.id):
        messages.success(request, 'product created succesfully')
    else:
        messages.success(request, 'something went wrong when creating a product!')

    return redirect('index_path')

def delete_product(request, product_id):
    p = Products.objects.get(pk=product_id)
    p.delete()
    if(p.id):
        messages.success(request, 'something went wrong!')
    else:
        messages.success(request, 'Product deleted successfully')
    return redirect('index_path')

def index(request):
    msgs = messages.get_messages(request)
    msg = ''
    for message in msgs:
        msg+=str(message)
        
    return render(request, 'index.html', {'products': get_products(), 'message': msg})

