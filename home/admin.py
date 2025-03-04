from django.contrib import admin
from .models import Index, FAQ, Team

# Register your models here.
@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

    
