from django.shortcuts import render


from .models import *

# Create your views here.

def base(request):
    return render(request, "base.html")


def get_products(request):
    products = Product.objects.all()
    
    context = {
        "products": products
    }
    
    return render(
        request,
        "product_review/products.html",
        context
    )
    
def get_product_info(request, prod_id: int):
    try: 
        product = Product.objects.get(id=prod_id)
    except:
        raise 
    
    
    context = {
        "product": product
    }
    
    return render(
        request, 
        "product_review/prod_info.html",
        context
    )
    

