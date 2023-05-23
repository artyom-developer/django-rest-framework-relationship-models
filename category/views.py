from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from category.models import CategoryModel
from category.serializers import CategorySerializer 

class CategoryApiView(APIView):
    def get(self, request):
        serializer = CategorySerializer(CategoryModel.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def post(self, request): 
        #res = request.data.get('name')  
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class CategoryApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return CategoryModel.objects.get(pk=pk)
        except CategoryModel.DoesNotExist:
            return None
    def get(self, request, id):
        data = self.get_object(id)
        serializer = CategorySerializer(data)  
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def put(self, request, id):
        data = self.get_object(id)
        if(data==None):
            return Response(status=status.HTTP_200_OK, data={ 'error': 'Not found data'})
        serializer = CategorySerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data) 
        return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)
    def delete(self, request, id):
        data = self.get_object(id)
        data.delete()
        response = { 'deleted': True }
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)
