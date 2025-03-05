from django.shortcuts import render
from .models import ProductORService

# Create your views here.
def products(request):
    product_item = ProductORService.objects.latest('updated_at')
    context = {
        "product":product_item
    }
    return render(request, 'products.html',context=context)
