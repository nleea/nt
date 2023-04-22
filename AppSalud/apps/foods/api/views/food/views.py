from rest_framework.views import APIView
from ...serializers.food_serializers import FoodSerializers,FoodSerializersView
from rest_framework.response import Response
from ....models.index import Food


class FoodView(APIView):
    def get(self,request,*args, **kwargs):
        serializers = FoodSerializersView(Food.objects.all(),many=True)
        return Response(serializers.data)


class CreateFood(APIView):
    def post(self,request,*args, **kwargs):
        serializers = FoodSerializers(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response("Ok")
        
        return Response(serializers.errors)

class UpdateFood(APIView):

    http_method_names = ["put"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
            

    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = Food.objects.get(pk=pk)
            return instance
        except Food.DoesNotExist:
            return None
    
    
    def put(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist",status=400)
        
        taskUpdate = FoodSerializers(instance=instanceOrNone,data=request.data,partial=True)
        
        if taskUpdate.is_valid():
            taskUpdate.save()
            return Response("Ok")
        
        return Response(taskUpdate.errors)


class DeleteFood(APIView):
    
    http_method_names = ["delete"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = Food.objects.get(pk=pk)
            return instance
        except Food.DoesNotExist:
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