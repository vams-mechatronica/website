from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('blog-details/<int:id>',views.blog_details,name="blog-detail-page"),
]