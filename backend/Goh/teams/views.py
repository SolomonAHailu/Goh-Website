from django.shortcuts import render
from rest_framework import permissions, viewsets
from teams.models import Team
from teams.permissions import IsAdminOrReadOnly
from teams.serializers import (TeamReadSerializer, TeamWriteSerializer)


class TeamViewSet(viewsets.ModelViewSet):
    
    queryset = Team.objects.all()
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return TeamWriteSerializer
        return TeamReadSerializer
    def get_permissions(self):
        if self.action in ("create","update", "partial_update", "destroy"):
            self.permission_classes = (IsAdminOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()