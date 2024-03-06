from django.shortcuts import render
from rest_framework import permissions, viewsets
from services.models import Service
from services.permissions import IsAdminOrReadOnly
from services.serializers import (ServiceReadSerializer, ServiceWriteSerializer)


class ServiceViewSet(viewsets.ModelViewSet):
    
    queryset = Service.objects.all()
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ServiceWriteSerializer
        return ServiceReadSerializer
    def get_permissions(self):
        if self.action in ("create","update", "partial_update", "destroy"):
            self.permission_classes = (IsAdminOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()