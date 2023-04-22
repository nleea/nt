from rest_framework import serializers
from apps.foods.models.index import Food
from .base_serializers import BaseSerializers

class FoodSerializersView(BaseSerializers):
    name = serializers.CharField()
    nutrients = serializers.CharField()
    carbohydrate = serializers.CharField()
    amount = serializers.IntegerField()
    list_food = serializers.SlugRelatedField("name",read_only=True)

class FoodSerializers(BaseSerializers):
    name = serializers.CharField()
    nutrients = serializers.CharField()
    carbohydrate = serializers.CharField()
    amount = serializers.IntegerField()
    list_food = serializers.IntegerField()
    
    
    class Meta:
        fields = "__all__"
    
    def create(self, validated_data):
        try:
            food = Food.objects.create(name=validated_data["name"],nutrients=validated_data["nutrients"],
                                       carbohydrate=validated_data["carbohydrate"],amount=validated_data["amount"],list_food_id=validated_data["list_food"])
            return food            
        except Exception as e:
            raise serializers.ValidationError(e.args)
    
    
    def update(self, instance, validated_data):
        try:
            instance.name=validated_data.get("name",instance.name)
            instance.nutrients=validated_data.get("nutrients",instance.nutrients)
            instance.carbohydrate=validated_data.get("carbohydrate",instance.carbohydrate)
            instance.amount=validated_data.get("amount",instance.amount)
            instance.list_food_id=validated_data.get("list_food",instance.list_food)
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(e.args)
