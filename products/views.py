from django.shortcuts import render
from .models import ProductORService

# Create your views here.
def proMonitor(request):
    product_item = ProductORService.objects.filter(name__icontains='ProMonitor')
    context = {
        "product":product_item
    }
    return render(request, 'products.html',context=context)
