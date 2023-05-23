from django.db import models
from django.db.models import SET_NULL 
from category.models import CategoryModel


class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField()
    published = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoryModel, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    