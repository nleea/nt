from rest_framework.views import APIView
from ..serializers.Taks_serializers import TaskSerializers
from rest_framework.response import Response
from ...models.models import Task

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
        
        return Response(serializers.errors)