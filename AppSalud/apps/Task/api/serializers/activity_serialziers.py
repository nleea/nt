from rest_framework import serializers
from ...models.models import Activity,ActivityType

class ActivityTypeSerializersView(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    
    class Meta:
        fields = "__All__"
        
    def create(self, validated_data):
        activityType = ActivityType.objects.create(name=validated_data["name"])
        return activityType
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.save()
        return instance

class ActivitySerializersView(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    listTask = serializers.SlugRelatedField("name",read_only=True)
    typeActivity = serializers.SlugRelatedField("name",read_only=True)
    repeat = serializers.BooleanField()
    
    class Meta:
        fields = "__all__"

class ActivitySerializers(serializers.Serializer):
    name = serializers.CharField()
    list_task = serializers.IntegerField()
    type_activity = serializers.IntegerField()
    repeat = serializers.BooleanField()
    
    class Meta:
        fields = "__all__"
    
    
    def create(self, validated_data):
        activity = Activity.objects.create(name=validated_data["name"],listTask_id=validated_data["list_task"],
                                       typeActivity_id=validated_data["type_activity"],repeat=validated_data["repeat"])
        return activity

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.listTask = validated_data.get("list_task",instance.listTask)
        instance.typeActivity = validated_data.get("type_activity",instance.typeActivity)
        instance.repeat = validated_data.get("repeat",instance.repeat)
        instance.save()
        return instance