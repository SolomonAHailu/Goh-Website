from rest_framework import serializers
from services.models import Service

class ServiceReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"

class ServiceWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = [
            "title",
            "description",
            "image",
            
        ]
        
    def create(self, validated_data):
        return Service.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance