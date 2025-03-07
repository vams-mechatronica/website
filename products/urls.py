from django.urls import path
from .views import *

urlpatterns = [
    path('promonitor',proMonitor,name="product-promonitor")
]
