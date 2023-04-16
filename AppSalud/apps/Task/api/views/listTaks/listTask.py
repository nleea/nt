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