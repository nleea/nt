from rest_framework import serializers
from ...models.models import ListTask
from .Taks_serializers import TaskSerializersView
from .activity_serialziers import ActivitySerializersView

class ListTaskSerializersView(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    priority = serializers.CharField()
    task = TaskSerializersView()
    
    class Meta:
        fields = "__all__"

class ListTaskSerializers(serializers.Serializer):
    priority = serializers.CharField()
    task = serializers.IntegerField()
    name = serializers.CharField()
    
    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        Listtask = ListTask.objects.create(task_id=validated_data["task"],priority=validated_data["priority"],name=validated_data["name"])
        return Listtask

    def update(self, instance, validated_data):
        instance.priority = validated_data.get("priority",instance.priority)
        instance.task = validated_data.get("task",instance.task)
        instance.save()
        return instance