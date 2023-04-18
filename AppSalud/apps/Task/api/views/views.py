from rest_framework.views import APIView
from ..serializers.Taks_serializers import TaskSerializers
from rest_framework.response import Response
from ...models.models import Task
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logger = logging.Logger("log")

class ViewTask(APIView):
    def get(self,request,*args, **kwargs):
        serializers = TaskSerializers(Task.objects.all(),many=True)
        return Response(serializers.data)


class CreateTask(APIView):
    def post(self,request,*args, **kwargs):
        serializers = TaskSerializers(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response("Ok")
        
        return Response(serializers.errors,status=400)


class UpdateTask(APIView):

    http_method_names = ["put"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
            
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = Task.objects.get(pk=pk)
            return instance
        except Task.DoesNotExist:
            return None
    
    
    def put(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist",status=400)
        
        taskUpdate = TaskSerializers(instance=instanceOrNone,data=request.data,partial=True)
        
        if taskUpdate.is_valid():
            taskUpdate.save()
            return Response("Ok")
        
        return Response(taskUpdate.errors,status=400)


class DeleteTask(APIView):
    
    http_method_names = ["delete"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = Task.objects.get(pk=pk)
            return instance
        except Task.DoesNotExist:
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