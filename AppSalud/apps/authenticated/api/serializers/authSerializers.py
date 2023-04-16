from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
    class Meta:
        fields = '__all__'
    
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is not None:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')


class RegisterSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    avatar = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    email=serializers.CharField()
    
    
    class Meta:
        fields = '__all__'
    
    
    def create(self, validated_data):
        try:
            return User.objects.create(**validated_data)
        except Exception:
            return None
    
    
    def update(self, instance, validated_data):
        try:
            instance.username = validated_data.get("username",instance.username)
            instance.password = validated_data.get("password",instance.password)
            instance.email = validated_data.get("email",instance.email)
            instance.avatar = validated_data.get("avatar",instance.avatar)
            instance.name = validated_data.get("name",instance.name)
            instance.last_name = validated_data.get("last_name",instance.last_name)
            instance.save()
            return instance
        except Exception:
            return None
    