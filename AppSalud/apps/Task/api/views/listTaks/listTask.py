from rest_framework.views import APIView
from ...serializers.list_Task_serializers import ListTaskSerializers,ListTaskSerializersView
from rest_framework.response import Response
from ....models.models import ListTask

class ListTaskView(APIView):
    def get(self,request,*args, **kwargs):
        serializers = ListTaskSerializersView(ListTask.objects.all(),many=True)
        return Response(serializers.data)


class CreateListTask(APIView):
    def post(self,request,*args, **kwargs):
        serializers = ListTaskSerializers(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response("Ok")
        
        return Response(serializers.errors)


class UpdateListTaks(APIView):

    http_method_names = ["put"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
            

    
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = ListTask.objects.get(pk=pk)
            return instance
        except ListTask.DoesNotExist:
            return None
    
    
    def put(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist",status=400)
        
        taskUpdate = ListTaskSerializers(instance=instanceOrNone,data=request.data,partial=True)
        
        if taskUpdate.is_valid():
            taskUpdate.save()
            return Response("Ok")
        
        return Response(taskUpdate.errors,status=400)


class DeleteListTask(APIView):
    
    http_method_names = ["delete"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = ListTask.objects.get(pk=pk)
            return instance
        except ListTask.DoesNotExist:
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