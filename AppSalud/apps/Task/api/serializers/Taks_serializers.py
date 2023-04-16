from rest_framework import serializers
from ...models.models import Task

class TaskSerializersView(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    priority = serializers.CharField()
    status = serializers.BooleanField()
    name = serializers.CharField()
    
    class Meta:
        fields = "__all__"

class TaskSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    priority = serializers.CharField()
    status = serializers.BooleanField()
    name = serializers.CharField()
    
    class Meta:
        fields = "__all__"
    
    def create(self, validated_data):
        try:
            task = Task.objects.create(name=validated_data["name"],priority=validated_data["priority"],status=validated_data["status"])
            return task
        except Exception:
            raise Exception("Error saved the record")

    def update(self, instance, validated_data):
        try:
            instance.priority = validated_data.get("priority",instance.priority)
            instance.status = validated_data.get("status",instance.status)
            instance.name = validated_data.get("name",instance.name)
            instance.save()
            return instance
        except Exception:
            raise Exception("Error updated the record")
