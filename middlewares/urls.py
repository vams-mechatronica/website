from django.urls import path
from .views import *



urlpatterns = [
    path("log/overview/",DataLogAPI.as_view(),name="overview"),
    path('log/graph/',getGraphOverview,name="get-graph-overview"),
    path('log/errors/',ErrorLogApi.as_view()),
    path("robots.txt", robots_txt, name="robots_txt"),
]