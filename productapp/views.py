from django.shortcuts import render
from django.core.paginator import Paginator 
from productapp.models import Product
# Create your views here.
def index(request):
    products=Product.objects.filter(isTranding=True)
    return render(request,"index.html",{"products":products})


def productDetail(request,id):
    product=Product.objects.get(pk=id)
    return render(request,"detail.html",{"product":product})


def products(request):
    all_products=Product.objects.all().order_by("name")
    #per page
    page=request.GET.get("page")
    paginator=Paginator(all_products,3)
    all_products=paginator.get_page(page)
    return render(request,"products.html",{"all_products":all_products})