from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from product.models import ProductModel
from product.serializers import ProductSerializer 
 
class ProductApiView(APIView):
    def get(self, request):
        queryset = ProductModel.objects.all()        
        if request.query_params.get('search'): 
            queryset = queryset.filter(name__icontains=request.query_params.get('search'))
        if request.query_params.get('category'):
            queryset = queryset.filter(category=request.query_params.get('category'))
        if request.query_params.get('published'):
            queryset = queryset.filter(published=request.query_params.get('published'))
        serializer = ProductSerializer( queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def post(self, request): 
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class ProductApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            return None
    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)  
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def put(self, request, id):
        product = self.get_object(id)
        if(product==None):
            return Response(status=status.HTTP_200_OK, data={ 'error': 'Not found data'})
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        response = { 'deleted': True }
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)        