from django.urls import path
from product.views import ProductApiView, ProductApiViewDetail
  
urlpatterns_product = [
    path('v1/product', ProductApiView.as_view()), 
    path('v1/product/<int:id>', ProductApiViewDetail.as_view()), 
]