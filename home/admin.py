from django.contrib import admin
from .models import Index, FAQ

# Register your models here.
@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    pass
    
