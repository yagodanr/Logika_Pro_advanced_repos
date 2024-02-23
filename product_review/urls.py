from django.urls import path

from .views import *


urlpatterns = [
    path("", get_products, name="products"),
    path("product/<int:prod_id>", get_product_info, name="prod_info"),
    
]