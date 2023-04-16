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