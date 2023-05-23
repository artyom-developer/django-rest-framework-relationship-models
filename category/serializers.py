from rest_framework import serializers
from category.models import CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = CategoryModel
        fields = ['id', 'name']