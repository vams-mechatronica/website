from django.urls import path
from .views import *

urlpatterns = [
    path('title',products,name="product-title")
]
