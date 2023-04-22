from rest_framework import serializers
from ...models.index import Foods
from .base_serializers import BaseSerializers


class FoodsSerilizersView(BaseSerializers):
    name = serializers.CharField()
    user_foods = serializers.SlugRelatedField("username",read_only=True)


class FoodsSerializers(BaseSerializers):
    name = serializers.CharField()
    user = serializers.IntegerField()
    
    
    class Meta:
        fields = "__all__"
    
    def create(self, validated_data):
        try:
            foods = Foods.objects.create(name=validated_data["name"],user_foods_id=validated_data["user"])
            return foods
        except Exception as e:
            raise serializers.ValidationError(e.args)
    
    
    def update(self, instance, validated_data):
       try:
            instance.name = validated_data.get("name",instance.name)
            instance.user_foods_id=validated_data.get("user",instance.user_foods)
            instance.save()
            return instance
       except Exception as e:
           raise serializers.ValidationError(e.args)
