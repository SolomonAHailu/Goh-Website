from rest_framework import serializers
from contact.models import Contact

class ContactReadSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source="author.get_full_name", read_only=True)
    class Meta:
        model = Contact
        fields = "__all__"

class ContactWriteSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "message",
            
        ]
        
    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance