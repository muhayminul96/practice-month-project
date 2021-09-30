from django.shortcuts import render
from django.http import HttpResponse
from pharma.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request,'index.html',context)


def product(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    if request.method =="GET":
        return render(request,'shop.html',context)
    elif request.method == "POST":
        name = request.POST['name']
        selected_product = Product.objects.get(slug = name)

        return render(request, 'shop-single.html', {'product': selected_product})


def selected_product(request,medicine_name):
    selected_product = Product.objects.get(slug=medicine_name)

    return render(request,'shop-single.html',{'product':selected_product})
