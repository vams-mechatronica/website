from django.contrib import admin
from .models import ProductORService


# Register your models here.
@admin.register(ProductORService)
class ProductORServiceAdmin(admin.ModelAdmin):
    pass
    
