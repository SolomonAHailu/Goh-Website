from django.shortcuts import render
from rest_framework import permissions, viewsets
from projects.models import Project
from projects.permissions import IsAdminOrReadOnly
from projects.serializers import (ProjectReadSerializer, ProjectWriteSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    
    queryset = Project.objects.all()
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ProjectWriteSerializer
        return ProjectReadSerializer
    def get_permissions(self):
        if self.action in ("create","update", "partial_update", "destroy"):
            self.permission_classes = (IsAdminOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()