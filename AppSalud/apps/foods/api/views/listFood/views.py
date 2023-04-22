from rest_framework.views import APIView
from ...serializers.list_food_serialsiers import ListFoodSerializers,ListFoodSerializersView
from rest_framework.response import Response
from ....models.index import ListFoods


class ListFoodsView(APIView):
    def get(self,request,*args, **kwargs):
        serializers = ListFoodSerializersView(ListFoods.objects.all(),many=True)
        return Response(serializers.data)


class CreateListFoods(APIView):
    def post(self,request,*args, **kwargs):
        serializers = ListFoodSerializers(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response("Ok")
        
        return Response(serializers.errors)

class UpdateListFoods(APIView):

    http_method_names = ["put"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
            

    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = ListFoods.objects.get(pk=pk)
            return instance
        except ListFoods.DoesNotExist:
            return None
    
    
    def put(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist",status=400)
        
        taskUpdate = ListFoodSerializers(instance=instanceOrNone,data=request.data,partial=True)
        
        if taskUpdate.is_valid():
            taskUpdate.save()
            return Response("Ok")
        
        return Response(taskUpdate.errors)


class DeleteListFoods(APIView):
    
    http_method_names = ["delete"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = ListFoods.objects.get(pk=pk)
            return instance
        except ListFoods.DoesNotExist:
            return None
    
    
    def delete(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist",status=400)

        try:
            instanceOrNone.delete()
        except Exception:
            return Response("Error",status=400)

        return Response("Ok")