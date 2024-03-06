from rest_framework import serializers
from projects.models import Project, Icon

class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = "__all__"

class ProjectReadSerializer(serializers.ModelSerializer):
   
    icon = IconSerializer()
    class Meta:
        model = Project
        fields = "__all__"

class ProjectWriteSerializer(serializers.ModelSerializer):
    icon = IconSerializer()
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
            "icon",
            
        ]
        
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance