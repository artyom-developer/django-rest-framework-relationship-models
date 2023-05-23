from django.urls import path
from category.views import CategoryApiView, CategoryApiViewDetail
  
urlpatterns_category = [
    path('v1/category', CategoryApiView.as_view()), 
    path('v1/category/<int:id>', CategoryApiViewDetail.as_view()), 
]