from rest_framework import serializers
from .base_serializers import BaseSerializers
from ...models.index import ListFoods

class ListFoodSerializersView(BaseSerializers):
    name = serializers.CharField()
    foods_list = serializers.SlugRelatedField("name",read_only=True)

class ListFoodSerializers(BaseSerializers):
    name = serializers.CharField()
    foods_list = serializers.IntegerField()
    
    def create(self, validated_data):
        try:
            return ListFoods.objects.create(name=validated_data["name"],foods_list_id=validated_data["foods_list"])
        except Exception as e:
            raise serializers.ValidationError(e.args)

    
    def update(self, instance, validated_data):
        try:
            instance.name=validated_data.get("name",instance.name)
            instance.foods_list_id =validated_data.get("foods_list",instance.foods_list)
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationErrore(e.args)