from rest_framework import serializers
from blogs.models import Blog

class BlogReadSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source="author.get_full_name", read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"

class BlogWriteSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Blog
        fields = [
            "title",
            "author",
            "content",
            "category",
            "tags",
            "image"
        ]
        
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance