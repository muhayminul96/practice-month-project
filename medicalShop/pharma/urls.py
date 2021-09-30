from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('product',product),
    path('product/<slug:medicine_name>/',selected_product),
]