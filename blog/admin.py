from django.contrib import admin
from .models import Blog, BlogTag, BlogCategories

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogCategories)
class BlogCategoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass
    

    

    
