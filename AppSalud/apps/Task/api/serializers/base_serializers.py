from rest_framework import serializers


class BaseSerializers(serializers.Serializer):
    name = serializers.CharField()
    createBy = serializers.SlugRelatedField("name",read_only=True)
    updateBy = serializers.SlugRelatedField("name",read_only=True)
    createAt = serializers.DateTimeField()
    updateAt = serializers.DateTimeField()
    
    
    
    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop('meta', None))
        
        super().__init__(instance, data, **kwargs)
        
        if not meta:
            self.fields.pop("createBy")
            self.fields.pop("updateBy")
            self.fields.pop("createAt")
            self.fields.pop("updateAt")