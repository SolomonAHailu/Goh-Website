from rest_framework import serializers
from teams.models import Team

class TeamReadSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source="author.get_full_name", read_only=True)
    class Meta:
        model = Team
        fields = "__all__"

class TeamWriteSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Team
        fields = [
            "first_name",
            "last_name",
            "job_title",
            "description",
            "image"
        ]
        
    def create(self, validated_data):
        return Team.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance