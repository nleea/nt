from rest_framework.views import APIView
from ...serializers.activity_serialziers import ActivitySerializersView,ActivityTypeSerializersView,ActivitySerializers
from rest_framework.response import Response
from ....models.models import Activity,ActivityType

class ActivityTypeVIew(APIView):
    def get(self,request,*args, **kwargs):
        serializers = ActivityTypeSerializersView(ActivityType.objects.all(),many=True)
        return Response(serializers.data)

class ActivityTypeCreate(APIView):
    def post(self,request,*args, **kwargs):
        serializers = ActivityTypeSerializersView(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response("Ok")
        
        return Response(serializers.errors)


class UpdateTypeActivity(APIView):

    http_method_names = ["put"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
            

    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = ActivityType.objects.get(pk=pk)
            return instance
        except ActivityType.DoesNotExist:
            return None
    
    
    def put(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist")
        
        taskUpdate = ActivityTypeSerializersView(instance=instanceOrNone,data=request.data,partial=True)
        
        if taskUpdate.is_valid():
            taskUpdate.save()
            return Response("Ok")
        
        return Response(taskUpdate.errors)


class DeleteTypeActivity(APIView):
    
    http_method_names = ["delete"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = ActivityType.objects.get(pk=pk)
            return instance
        except ActivityType.DoesNotExist:
            return None
    
    
    def delete(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist")

        try:
            instanceOrNone.delete()
        except Exception:
            return Response("Error")

        return Response("Ok")


class ActivityView(APIView):
    def get(self,request,*args, **kwargs):
        serializers = ActivitySerializersView(Activity.objects.all(),many=True)
        return Response(serializers.data)


class CreateActivity(APIView):
    def post(self,request,*args, **kwargs):
        serializers = ActivitySerializers(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response("Ok")
        
        return Response(serializers.errors)

class UpdateActivity(APIView):

    http_method_names = ["put"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
            

    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = Activity.objects.get(pk=pk)
            return instance
        except Activity.DoesNotExist:
            return None
    
    
    def put(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist")
        
        taskUpdate = ActivitySerializers(instance=instanceOrNone,data=request.data,partial=True)
        
        if taskUpdate.is_valid():
            taskUpdate.save()
            return Response("Ok")
        
        return Response(taskUpdate.errors)


class DeleteActivity(APIView):
    
    http_method_names = ["delete"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    
    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            instance = Activity.objects.get(pk=pk)
            return instance
        except Activity.DoesNotExist:
            return None
    
    
    def delete(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("Do not Exist")

        try:
            instanceOrNone.delete()
        except Exception:
            return Response("Error")

        return Response("Ok")