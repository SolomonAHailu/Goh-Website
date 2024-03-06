from django.shortcuts import render
from rest_framework import permissions, viewsets
from contact.models import Contact
from contact.permissions import IsAdminOrReadOnly
from contact.serializers import (ContactReadSerializer, ContactWriteSerializer)


class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ContactWriteSerializer
        return ContactReadSerializer
    def get_permissions(self):
        if self.action in ("create","update"):
            self.permission_classes = (permissions.AllowAny,)
        else:
            self.permission_classes = (IsAdminOrReadOnly,)

        return super().get_permissions()